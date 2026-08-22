"""Pull the README sections that coverage analysis depends on.

Sections are kept verbatim. The skill judges "does this tool do what I need"
against the maintainer's own words, so paraphrasing here would quietly corrupt
every coverage answer downstream.
"""

from __future__ import annotations

import re

WANTED = {
    "features": ("feature", "what it does", "capabilities", "overview", "why "),
    "installation": ("install", "setup", "getting started", "quick start", "quickstart"),
    "tools": ("tools", "commands", "api", "usage", "examples"),
    "configuration": ("config", "options", "environment"),
    "limitations": ("limitation", "caveat", "known issue", "not supported", "roadmap"),
    "requirements": ("requirement", "prerequisite", "dependencies"),
}

ATX_HEADING = re.compile(r"^#{1,3}[ \t]+(.+?)[ \t]*$", re.MULTILINE)
# reStructuredText and setext markdown underline their headings instead. Many
# Python projects ship .rst READMEs, and a markdown-only parser produced no
# sections at all for them, so they got no detail file and no install command.
UNDERLINE_HEADING = re.compile(
    r"^(?P<title>[^\s\n][^\n]{0,78})\n(?P<rule>[=\-~^\"'`*+#]{3,})[ \t]*$", re.MULTILINE
)
FENCE = re.compile(r"```[a-zA-Z]*\n(.*?)```", re.DOTALL)
# ".. code:: bash" and a bare "::" both introduce an indented literal block.
RST_BLOCK = re.compile(r"::[^\n]*\n\n((?:[ \t]+[^\n]*\n?)+)")
MAX_SECTION = 4_000

INSTALL_MARKERS = (
    "plugin marketplace add",
    "plugin install",
    "npm install",
    "npx ",
    "pnpm add",
    "yarn add",
    "pip install",
    "uv add",
    "uvx ",
    "pipx install",
    "brew install",
    "cargo install",
    "go install",
    "docker run",
    "claude mcp add",
)


def _canonical(heading: str) -> str | None:
    lowered = heading.lower()
    for canonical, needles in WANTED.items():
        if any(needle in lowered for needle in needles):
            return canonical
    return None


def _headings(text: str) -> list:
    """Every heading in the document, in order, whichever style it uses."""
    found = [(match.start(), match.end(), match.group(1)) for match in ATX_HEADING.finditer(text)]

    for match in UNDERLINE_HEADING.finditer(text):
        title = match.group("title").strip()
        # The underline must be at least as long as the title it underlines,
        # which is what separates a real heading from a horizontal rule.
        if len(match.group("rule")) >= len(title) and not title.startswith(("-", "=", "|")):
            found.append((match.start(), match.end(), title))

    found.sort(key=lambda item: item[0])
    return found


def extract_sections(markdown: str) -> dict[str, str]:
    matches = _headings(markdown)
    sections: dict[str, str] = {}

    for index, (_, heading_end, title) in enumerate(matches):
        canonical = _canonical(title)
        if not canonical or canonical in sections:
            continue
        start = heading_end
        end = matches[index + 1][0] if index + 1 < len(matches) else len(markdown)
        body = markdown[start:end].strip()
        if body:
            sections[canonical] = body[:MAX_SECTION]

    return sections


def has_install_section(markdown: str) -> bool:
    return "installation" in extract_sections(markdown)


def extract_install_command(markdown: str) -> str:
    """The one line a user would actually paste, or empty when there is none."""
    section = extract_sections(markdown).get("installation")
    if not section:
        return ""

    lines = []
    for block in FENCE.findall(section) + RST_BLOCK.findall(section):
        for line in block.splitlines():
            cleaned = line.strip().lstrip("$").strip()
            if cleaned and not cleaned.startswith("#"):
                lines.append(cleaned)

    for line in lines:
        if any(marker in line for marker in INSTALL_MARKERS):
            return line[:200]

    return lines[0][:200] if lines else ""
