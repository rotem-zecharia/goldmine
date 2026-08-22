# K-Dense-AI/scientific-agent-skills

Turn any AI agent into an AI Scientist. The #1 Agent Skills library for science, used by 175,000+ scientists worldwide. 163 ready-to-use validated skills plus 100+ scientific databases covering biolog

## features

### ⚡ **Accelerate Your Research**
- **Save Days of Work** - Skip API documentation research and integration setup
- **Reviewed Starting Points** - Tested examples with explicit validation, provenance, and safety boundaries; verify them in the target environment
- **Multi-Step Workflows** - Execute complex pipelines with a single prompt

### 🎯 **Comprehensive Coverage**
- **161 Skills** - Extensive coverage across all major scientific domains
- **100+ Databases** - Unified access to 78+ databases via database-lookup, plus dedicated data access skills and multi-database packages like BioServices, BioPython, and gget
- **70+ Optimized Python Package Skills** - Current, version-scoped guidance for packages including RDKit, Scanpy, PyTorch Lightning, scikit-learn, PyTDC, pydicom, PufferLib, QuTiP, GeoPandas, pymatgen, Qiskit, Molecular Dynamics (OpenMM/MDAnalysis), scVelo, and TimesFM (the agent can use any Python package; these are the pre-documented paths)

### 🔧 **Easy Integration**
- **Simple Setup** - Copy skills to your skills directory and start working
- **Configured Discovery** - Compatible hosts can find and use relevant skills from their configured skill paths
- **Well Documented** - Each skill includes examples, use cases, and best practices

### 🌟 **Maintained & Supported**
- **Regular Updates** - Continuously maintained and expanded by K-Dense team
- **Tested in CI** - Every skill that ships `scripts/` has a suite under `tests/`, plus a repo-wide structural contract (frontmatter, link resolution, script parsing, `--help` behavior) that runs on every pull request
- **Community Driven** - Open source with active community contributions
- **Enterprise Ready** - Commercial support available for advanced needs

---

## installation

### Option 1: npx (supported hosts)

Install Scientific Agent Skills with a single command:

```bash
npx skills add K-Dense-AI/scientific-agent-skills
```

This is a common standards-based installer for supported Agent Skills hosts, including current versions of **Claude Code**, **Claude Cowork**, **Codex**, **Gemini CLI**, **Google Antigravity**, and **Cursor**. Confirm installation paths and optional metadata behavior in your host's current documentation.

### Option 2: GitHub CLI (`gh skill`)

If you use the [GitHub CLI](https://cli.github.com/) (v2.90.0+), you can install skills with [`gh skill`](https://github.blog/changelog/2026-04-16-manage-agent-skills-with-github-cli/):

```bash
# Browse and install interactively
gh skill install K-Dense-AI/scientific-agent-skills

# Install a specific skill directly
gh skill install K-Dense-AI/scientific-agent-skills scanpy

# Target a specific agent host
gh skill install K-Dense-AI/scientific-agent-skills --agent cursor
gh skill install K-Dense-AI/scientific-agent-skills --agent claude-code
gh skill install K-Dense-AI/scientific-agent-skills --agent codex
gh skill install K-Dense-AI/scientific-agent-skills --agent gemini
```

`gh skill` automatically installs to the correct directory for your agent host and records provenance metadata for supply chain integrity.

#### Version pinning

Pin to a specific release tag or commit SHA for reproducible installs:

```bash
# Pin to a release tag
gh skill install K-Dense-AI/scientific-agent-skills --pin v2.64.0

# Pin to a commit SHA
gh skill install K-Dense-AI/scientific-agent-skills --pin abc123def
```

#### Keeping skills up to date

```bash
# Check for updates interactively
gh skill update

# Update all installed skills
gh skill update --all
```

### Option 3: Agent Plugins (Cursor, Codex, and other plugin clients)

This repository is a valid [Agent Plugins](https://agent-plugins.org/) 1.0.0 package: root [`plugin.json`](plugin.json) plus Agent Skills under `skills/`. Clients that support the standard discover every immediate child of `skills/` that contains a `SKILL.md`.

**Cursor** — symlink or copy the repo into the local plugins directory, then reload:

```bash
mkdir -p ~/.cursor/plugins/local
ln -s "$(pwd)" ~/.cursor/plugins/local/scientific-agent-skills
```

Restart Cursor or run **Developer: Reload Window**, then confirm the plugin and its skills appear under **Customize**. See [Cursor plugins](https://cursor.com/docs/plugins).

**Codex** — install from a local checkout (confirm the current CLI flag names in Codex docs):

```bash
codex plugins install .
```

Compatible clients (Cursor, Codex, GitHub Copilot, VS Code, Kiro, and others listed at [agent-plugins.org](https://agent-plugins.org/compatible-clients)) share the same package layout; installation UX stays client-specific.

### Other Agent Skills hosts (OpenClaw, NemoClaw, Pi, Hermes, …)

Agent hosts differ in install paths, discovery settings, and support for optional frontmatter fields. `npx skills add` (Option 1) commonly installs into the `~/.agents/skills/` convention, with project-scoped installs under `.agents/skills/`; confirm both paths against your host's current documentation. To install manually on a host configured to scan one of those locations:

```bash
git clone https://github.com/K-Dense-AI/scientific-agent-skills.git ~/.agents/skills/scientific-agent-skills   # user-level
git clone https://github.com/K-Dense-AI/scientific-agent-skills.git .agents/skills/scientific-agent-skills      # project-level
```

For Hermes versions that support skill taps, add the repository as a tap:

```bash
hermes skills tap add K-Dense-AI/scientific-agent-skills
```

Every `SKILL.md` has YAML frontmatter, but legacy and community skills vary in `metadata` formatting (block or flow style) and optional extension fields. Repository updates must keep `metadata.version` as a quoted numeric string and pass canonical `skills-ref validate ./skills/<skill-name>` checks. Hosts may interpret o

## requirements

- **Python**: 3.13+ for repository tooling; individual skill dependencies may support broader Python ranges
- **uv**: Python package manager (required for installing skill dependencies)
- **Client**: Any agent that supports the [Agent Skills](https://agentskills.io/) standard (Cursor, Claude Code, Gemini CLI, Codex, Google Antigravity, etc.)
- **System**: macOS, Linux, or Windows with WSL2
- **Dependencies**: Automatically handled by individual skills (check `SKILL.md` files for specific requirements)

## tools

Once you've installed the skills, you can ask your AI agent to execute complex multi-step scientific workflows. Here are some example prompts:

### 🧪 Drug Discovery Pipeline
**Goal**: Prioritize EGFR inhibitor candidates for preclinical lung-cancer research

**Prompt**:
```
Use available skills you have access to whenever possible. Query ChEMBL for EGFR inhibitors (IC50 < 50nM), analyze structure-activity relationships 
with RDKit, generate improved analogs with datamol, perform virtual screening with DiffDock 
against AlphaFold EGFR structure, search PubMed for resistance mechanisms, check COSMIC for 
mutations, and create visualizations and a comprehensive report.
```

**Skills Used**: database-lookup, rdkit, datamol, diffdock, paper-lookup, scientific-visualization

---

### 🔬 Single-Cell RNA-seq Analysis
**Goal**: Comprehensive analysis of 10X Genomics data with public data integration

**Prompt**:
```
Use available skills you have access to whenever possible. Load 10X dataset with Scanpy, perform QC and doublet removal, integrate with Cellxgene 
Census data, identify cell types using NCBI Gene markers, run differential expression with 
PyDESeq2, infer gene regulatory networks with Arboreto, enrich pathways via Reactome/KEGG, 
and identify therapeutic targets with Open Targets.
```

**Skills Used**: scanpy, cellxgene-census, database-lookup, pydeseq2, arboreto

---

### 🧬 Multi-Omics Biomarker Discovery
**Goal**: Integrate RNA-seq, proteomics, and metabolomics to predict patient outcomes

**Prompt**:
```
Use available skills you have access to whenever possible. Analyze RNA-seq with PyDESeq2, process mass spec with pyOpenMS, integrate metabolites from 
HMDB/Metabolomics Workbench, map proteins to pathways (UniProt/KEGG), find interactions via 
STRING, correlate omics layers with statsmodels, build predictive model with scikit-learn, 
and search ClinicalTrials.gov for relevant trials.
```

**Skills Used**: pydeseq2, pyopenms, database-lookup, statsmodels, scikit-learn

---

### 🎯 Virtual Screening Campaign
**Goal**: Discover allosteric modulators for protein-protein interactions

**Prompt**:
```
Use available skills you have access to whenever possible. Retrieve AlphaFold structures, identify interaction interface with BioPython, search ZINC 
for allosteric candidates (MW 300-500, logP 2-4), filter with RDKit, dock with DiffDock, 
rank with DeepChem, check PubChem suppliers, search USPTO patents, and optimize leads with 
MedChem/molfeat.
```

**Skills Used**: database-lookup, biopython, rdkit, diffdock, deepchem, medchem, molfeat

---

### 🏥 Research Variant Evidence Review
**Goal**: Annotate a synthetic or properly de-identified VCF for hereditary-cancer research and qualified review

**Prompt**:
```
Use available skills you have access to whenever possible. Work only with authorized synthetic
or de-identified data. Parse the VCF with pysam, annotate variants with Ensembl VEP, retrieve
ClinVar/COSMIC/NCBI Gene/UniProt evidence, and verify literature sources. Build an evidence-
traceable research summary with scientific-writing. If clinical-reports is used, create only a
visibly marked draft structure from a verified source-fact manifest for qualified review; do not
diagnose, assess individual risk, recommend treatment, or determine trial eligibility.
```

**Skills Used**: pysam, database-lookup, paper-lookup, scientific-writing, clinical-reports

---

### 🌐 Systems Biology Network Analysis
**Goal**: Analyze gene regulatory networks from RNA-seq data

**Prompt**:
```
Use available skills you have access to whenever possible. Query NCBI Gene for annotations, retrieve sequences from UniProt, identify interactions via 
STRING, map to Reactome/KEGG pathways, analyze topology with Torch Geometric, reconstruct 
GRNs with Arboreto, assess druggability with Open Targets, model with PyMC, visualize 
networks, and search GEO for similar patterns.
```

**Skills Used**: database-lookup, torch-geometric, arboreto, pymc, networkx, scient

## configuration

uv run python tests/run_all.py --isolated
```

The [Skill Tests](https://github.com/K-Dense-AI/scientific-agent-skills/actions/workflows/skill-tests.yml) workflow runs the contract plus the standard-library-only suites on every pull request; the full `--isolated` sweep builds ~100 environments and is run locally or on a schedule.

### Security Scanning

All skills in this repository are security-scanned using [Cisco AI Defense Skill Scanner](https://github.com/cisco-ai-defense/skill-scanner), an open-source tool that detects prompt injection, data exfiltration, and malicious code patterns in Agent Skills.

If you are contributing a new skill, we recommend running the scanner locally before submitting a pull request:

```bash
uv pip install cisco-ai-skill-scanner
skill-scanner scan /path/to/your/skill --use-behavioral
```

> **Note:** A clean scan result reduces noise in review, but does not guarantee a skill is free of all risk. Contributed skills are also reviewed manually before merging.

### Recognition

Contributors are recognized in our community and may be featured in:
- Repository contributors list
- Special mentions in release notes
- K-Dense community highlights

Your contributions help make scientific computing more accessible and enable researchers to leverage AI tools more effectively!

### Support Open Source

This project builds on 50+ amazing open source projects. If you find value in these skills, please consider [supporting the projects we depend on](docs/open-source-sponsors.md).

---

## 🔧 Troubleshooting

### Common Issues

**Problem: Skills not loading**
- Verify skill folders are in the correct directory (see [Getting Started](#-getting-started))
- Each skill folder must contain a `SKILL.md` file
- Restart your agent/IDE after copying skills
- In Cursor, check Settings → Rules to confirm skills are discovered

**Problem: Missing Python dependencies**
- Solution: Check the specific `SKILL.md` file for required packages
- Install dependencies: `uv pip install package-name`

**Problem: API rate limits**
- Solution: Many databases have rate limits. Review the specific database documentation
- Consider implementing caching or batch requests

**Problem: Authentication errors**
- Solution: Some services require API keys. Check the `SKILL.md` for authentication setup
- Verify your credentials and permissions

**Problem: Outdated examples**
- Solution: Report the issue via GitHub Issues
- Check the official package documentation for updated syntax

**Problem: `gh skill install` or docs link to `scientific-skills/` fails (v2.43.0+)**
- As of v2.43.0, skills live under `skills/` (not `scientific-skills/`) to match the Agent Skills layout expected by GitHub CLI
- Update manual copy paths, bookmarks, and citations from `scientific-skills/<name>` to `skills/<name>`
- Re-run `gh skill install K-Dense-AI/scientific-agent-skills` after pulling the latest release

---

## ❓ FAQ

### General Questions

**Q: Is this free to use?**  
A: Yes! This repository is MIT licensed. However, each individual skill has its own license specified in the `license` metadata field within its `SKILL.md` file—be sure to review and comply with those terms.

**Q: Why are all skills grouped together instead of separate packages?**  
A: We believe good science in the age of AI is inherently interdisciplinary. Bundling all skills together makes it trivial for you (and your agent) to bridge across fields—e.g., combining genomics, cheminformatics, clinical data, and machine learning in one workflow—without worrying about which individual skills to install or wire together.

**Q: Can I use this for commercial projects?**  
A: The repository itself is MIT licensed, which allows commercial use. However, individual skills may have different licenses—check the `license` field in each skill's `SKILL.md` file to ensure compliance with your intended use.

**Q: Do all skills have the same license?**  
A: No. Each skill has its own license specified in the `li
