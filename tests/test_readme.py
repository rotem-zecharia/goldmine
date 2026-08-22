from goldmine.readme import extract_install_command, extract_sections, has_install_section

README = """# claude-video-vision

Give Claude the ability to watch and understand videos.

## Features

- Frame extraction at configurable intervals
- Per-frame vision analysis
- Audio transcription

## Installation

```bash
claude plugin install claude-video-vision
```

## Tools

- `analyze_video` - full analysis
- `extract_frames` - frames only

## Limitations

- Does not download from social platforms
- Requires ffmpeg on PATH

## Licence

MIT
"""


def test_extracts_the_sections_coverage_analysis_needs():
    sections = extract_sections(README)

    assert {"features", "installation", "tools", "limitations"} <= set(sections)


def test_section_text_is_verbatim_not_summarised():
    assert "Per-frame vision analysis" in extract_sections(README)["features"]


def test_limitations_are_preserved_because_gaps_matter_most():
    assert "Does not download from social platforms" in extract_sections(README)["limitations"]


def test_ignores_boilerplate_sections():
    assert "licence" not in extract_sections(README)


def test_returns_empty_for_an_empty_readme():
    assert extract_sections("") == {}


def test_handles_a_readme_with_no_headings():
    assert extract_sections("just some prose with no structure") == {}


def test_detects_an_install_section():
    assert has_install_section(README) is True


def test_detects_a_missing_install_section():
    assert has_install_section("# tool\n\nsome prose\n") is False


def test_truncates_a_very_long_section():
    long_readme = "# t\n\n## Features\n\n" + ("x" * 20_000)

    assert len(extract_sections(long_readme)["features"]) <= 4_000


def test_extracts_the_install_command_from_a_fenced_block():
    assert extract_install_command(README) == "claude plugin install claude-video-vision"


def test_install_command_skips_a_shell_prompt_marker():
    readme = "## Install\n\n```sh\n$ pip install thing\n```\n"

    assert extract_install_command(readme) == "pip install thing"


def test_install_command_prefers_a_recognisable_package_manager_line():
    readme = "## Install\n\n```bash\ncd myproject\nnpm install -g thing\n```\n"

    assert extract_install_command(readme) == "npm install -g thing"


def test_install_command_is_empty_when_there_is_no_install_section():
    assert extract_install_command("# tool\n\nprose\n") == ""


def test_extracts_a_claude_plugin_marketplace_command():
    readme = "## Setup\n\n```\n/plugin marketplace add owner/repo\n```\n"

    assert "plugin marketplace add" in extract_install_command(readme)


def test_headings_with_emoji_and_anchors_still_match():
    readme = "## \U0001f680 Quick Start\n\nrun it\n"

    assert "installation" in extract_sections(readme)


RST = """gallery-dl
==========

Download image galleries from several sites.

Features
--------

- Supports Instagram, Twitter, Pixiv and many more
- Resumable downloads

Installation
------------

.. code:: bash

    pip install gallery-dl
"""


def test_extracts_sections_from_restructuredtext():
    # gallery-dl and many Python projects ship .rst READMEs with underlined
    # headings; a markdown-only parser produced no detail file at all for them.
    sections = extract_sections(RST)

    assert "features" in sections and "installation" in sections


def test_restructuredtext_section_text_is_verbatim():
    assert "Supports Instagram" in extract_sections(RST)["features"]


def test_setext_markdown_headings_are_recognised():
    markdown = "Tool\n====\n\nFeatures\n--------\n\n- does things\n"

    assert "does things" in extract_sections(markdown)["features"]


def test_an_underline_that_is_not_a_heading_is_ignored():
    # A table rule or horizontal line must not create a phantom section.
    text = "# Tool\n\nsome prose\n\n-----\n\nmore prose\n"

    assert extract_sections(text) == {}


def test_install_command_is_found_in_an_rst_code_block():
    assert extract_install_command(RST) == "pip install gallery-dl"
