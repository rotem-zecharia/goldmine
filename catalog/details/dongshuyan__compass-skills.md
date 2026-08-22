# dongshuyan/compass-skills

司南：个性化 AI 任务总控 Skills 系统 /COMPASS: Personal Alignment Skills OS for AI Agents

## installation

List the available skills before installing:

```bash
npx skills add dongshuyan/compass-skills --list
```

Install all skills for Claude Code:

```bash
npx skills add dongshuyan/compass-skills --skill '*' -a claude-code
```

Install all skills for both Codex and Claude Code:

```bash
npx skills add dongshuyan/compass-skills --skill '*' -a codex -a claude-code
```

After installation, invoke the skills directly in an AI conversation:

```text
$task-clarifier
$task-forest
$session-handoff-prompt
$user-profile-keeper
$run-history-skill-builder
$run-history-skill-upgrader
$academic-humanizer
```

For manual installation, copy the seven folders under [`skills/`](skills/) into the agent's local skills directory and keep their `references/`, `scripts/`, `evals/`, and `agents/` subdirectories intact.

## features

Long-running agent work needs four kinds of state:

- User context: communication preferences, risk boundaries, recurring omissions, and collaboration style.
- Project context: where the current request fits, what it depends on, and how far it has progressed.
- Goal context: how the current task contributes to the original objective and whether it still matches it.
- Handoff context: what a new AI conversation needs to continue the current task without replaying the whole transcript.

COMPASS organizes that state into four local workflows:

1. A local profile that the user can inspect and correct.
2. A repo-local task graph that survives AI conversation boundaries.
3. A paste-ready continuation prompt for a new AI conversation.
4. A clarification gate before ambiguous or risky execution.

## How The Core And Meta Skills Work Together

`task-clarifier` is the entry point for ambiguous, high-cost, high-risk, evidence-sensitive, or externally visible work. It first identifies the user-owned decisions that must be made, asks 1-3 focused questions with recommended answers, confirms shared understanding, and only then searches or executes.

`task-forest` records long-running work structure: why a task exists, where it fits, how far it progressed, what changed, and what remains unresolved.

`session-handoff-prompt` turns the current AI conversation, explicit transcripts, workspace evidence, and optional task-forest exports into a concise prompt for the next AI conversation. It reads task-forest as structured context but never modifies it.

`user-profile-keeper` stores collaboration preferences locally. Future AI conversations use the profile to ask relevant questions and apply the right risk boundary. Current files, logs, and user-provided context remain the authority; secrets stay out of the profile.

`run-history-skill-builder` turns a completed or repeatedly refined workflow into a new skill package or a plan-only design. If the request is really about changing an existing skill, it hands the job off instead of editing that skill directly.

`run-history-skill-upgrader` takes the next step for existing skills: it automatically reads session evidence from real execution, encountered and resolved difficulties, validation results, and user feedback, then produces a concrete upgrade plan and stops. Only after explicit approval of that plan does it edit files. In practice, this is the simplest controlled self-evolution loop for skills: periodically run a target skill, accumulate real session evidence, then let the upgrader turn that evidence into a reviewed upgrade plan and, after approval, an applied change.

`academic-humanizer` helps authors avoid AI-sounding language while drafting and remove it from existing academic prose. It targets formulaic, vacuous, mechanically repetitive, and process-leaking patterns while protecting claims, evidence strength, quotations, formulas, citations, technical names, modality, logic, and scope. The result aims to read as natural, credible scholarly writing and to reduce the likelihood that readers perceive it as AI-generated; it does not promise a universal authorship judgment.

```text
user-profile-keeper    -> who is the user and how should we collaborate?
task-forest            -> where does this task fit and is it still aligned?
session-handoff-prompt -> what should the next AI conversation know to continue now?
task-clarifier         -> what should the agent do now?
run-history-skill-builder  -> how do we package this proven workflow as a new skill?
run-history-skill-upgrader -> how does a skill self-evolve safely from real session evidence?
academic-humanizer         -> how do we remove AI-sounding prose without changing its claims?
```

## Task Clarifier Example

A vague request is turned into a checked requirement before the agent recommends anything.

<details>
<summary>Example: choosing a suitcase</summary>

Formatted from a live terminal run. Terminal status lines are omitted.

### Turn 1

## requirements

**$task-clarifier**

> You need a checked suitcase for frequent business travel. The bag should be hard-shell for maximum durability and professional appearance, 28 inches for extended trips, and within a $300-600 budget. Durability is your top priority over lighter weight or organizational gimmicks.

**Inferences to confirm**

- Durability means repeated airport handling and 5+ years without major failure.
- Brand, color, wheel type, TSA lock, and warranty length are not yet fixed preferences.
- The next step is specific model recommendations, unless the user prefers an evaluation framework.

</details>

## Screenshots

Task forest HTML export:

![task-forest tree demo](assets/task-forest-demo.gif)

Live DAG view:

![task-forest live DAG view](assets/task-forest-live-dag.png)

Task detail view:

![task-forest live detail view](assets/task-forest-live-detail.png)

User profile and alignment flow:

![COMPASS user profile and alignment flow](assets/profile-alignment-flow.en.png)

Ecosystem map:

![COMPASS skills ecosystem DAG](assets/compass-system-map.en.svg)

## Compatibility

COMPASS works across agent runtimes as a `SKILL.md` package with Markdown instructions, YAML frontmatter, optional `references/`, optional `scripts/`, and optional agent metadata.

| Agent / environment | Recommended setup |
| --- | --- |
| Claude Code | Use `npx skills add dongshuyan/compass-skills --skill '*' -a claude-code`, or copy the folders under `skills/` into Claude Code's custom skills directory. |
| Codex | Use the `skills` CLI with `-a codex` when supported by your environment, or use the repo as a local skills source. |
| OpenCode / OpenClaw / other agents | Keep [`AGENTS.md`](AGENTS.md) and load the matching `SKILL.md` first, then use `references/` and `scripts/` as needed. |

The scripts use Python standard-library components and run locally.

## Safety Model

COMPASS keeps runtime data local:

- No upload of task data or user-profile data.
- No browser cookie, token, private key, credential, or session extraction.
- `task-forest` stores task data under the current workspace, usually `.agent-workbench/task-forest/`.
- `session-handoff-prompt` is read-only by default. It can validate local handoffs with real workspace paths or redact them for shareable handoffs.
- `user-profile-keeper` stores local profile data under `.compass-skills/user-profiles/v1` by default, or a user-selected `COMPASS_USER_PROFILE_HOME`.
- `run-history-skill-builder` reads only user-authorized workflow history and writes new skill files only to a user-approved local directory.
- `run-history-skill-upgrader` is plan-only by default. It can synthesize real session evidence into an upgrade plan automatically, but it enables a controlled self-evolution loop only after explicit approval of a concrete plan.
- `academic-humanizer` preserves source claims and locked spans, never invents facts or citations, and uses its Python script only for optional read-only diagnostics.
- High-risk actions such as deletion, overwrite, publishing, remote writes, credential use, and global configuration changes require explicit confirmation.

Important: `user-profile-keeper` uses local plaintext storage without encryption. Do not store passwords, tokens, private keys, verification codes, or highly sensitive personal data in the profile.

See [SECURITY.md](SECURITY.md) for the security boundary.

## Example Prompts

Clarify a task before execution:

```text
Use $task-clarifier to align the task below.

Task: ...
Material: ...
Constraints: ask user-owned decisions first; infer discoverable facts from files, context, or reliable sources. Ask only questions that change scope, method, evidence, format, safety, or acceptance criteria.
Output: ask 1-3 key questions with recommended answers first; once the core need is clear, restate your understanding in 2-5 lines and ask me to confirm.
```

Maintain the task forest for a workspace:

```text
Use $task-forest to analyze the current AI conversation a

## limitations

Planned additions:

- Build reusable skills from real task histories.
- Upgrade existing skills from observed failures, feedback, and validation evidence.
- Summarize local agent states, waiting-human items, risks, and review queues.
- Recommend low-switching-cost follow-up tasks from the task graph.

## License

MIT. See [LICENSE](LICENSE).

## Community

- This repo has been shared as open source on [Linux.do](https://linux.do/).

## Star History

<a href="https://www.star-history.com/?repos=dongshuyan%2Fcompass-skills&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=dongshuyan/compass-skills&type=date&theme=dark&legend=top-left&sealed_token=ajhWVt2plnutoF4MD46b_S2ubeT0JeSS9odrIX5tNCKKNTN3ewXPpRSdOknfBzsUZozj47FDTaUzfVv-xY9hMUekFfG68Ix9WXqHLufTnF-ClWcDSNbKrVDOgpHLTBpOhbn92V7J6J1dwCO-I_-SP_0rrTt9KAhmf6jEMZMrdQdVCMP2vOKgl9sx7aH0" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=dongshuyan/compass-skills&type=date&legend=top-left&sealed_token=ajhWVt2plnutoF4MD46b_S2ubeT0JeSS9odrIX5tNCKKNTN3ewXPpRSdOknfBzsUZozj47FDTaUzfVv-xY9hMUekFfG68Ix9WXqHLufTnF-ClWcDSNbKrVDOgpHLTBpOhbn92V7J6J1dwCO-I_-SP_0rrTt9KAhmf6jEMZMrdQdVCMP2vOKgl9sx7aH0" />
   <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=dongshuyan/compass-skills&type=date&legend=top-left&sealed_token=ajhWVt2plnutoF4MD46b_S2ubeT0JeSS9odrIX5tNCKKNTN3ewXPpRSdOknfBzsUZozj47FDTaUzfVv-xY9hMUekFfG68Ix9WXqHLufTnF-ClWcDSNbKrVDOgpHLTBpOhbn92V7J6J1dwCO-I_-SP_0rrTt9KAhmf6jEMZMrdQdVCMP2vOKgl9sx7aH0" />
 </picture>
</a>
