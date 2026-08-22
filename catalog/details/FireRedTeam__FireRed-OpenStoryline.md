# FireRedTeam/FireRed-OpenStoryline

FireRed-OpenStoryline is an AI video editing agent that transforms manual editing into intention-driven directing through natural language interaction, LLM-powered planning, and precise tool orchestra

## features

- 🌐 **Smart Media Search & Organization**: Automatically searches online and downloads images and video clips that match your requirements. Performs clip segmentation and content understanding based on your thematic media.
- ✍️ **Intelligent Script Generation**: Combines user themes, visual understanding, and emotion recognition to automatically construct storylines and context-aware narration. Features built-in Few-shot style transfer capabilities, allowing users to define specific copy styles (e.g., product reviews, casual vlogs) via reference text, achieving precise replication of tone, rhythm, and sentence structure.
- 🎵 **Intelligent Music, Voiceover & Font Recommendations**: Supports personal playlist imports and auto-recommends BGM based on content and mood, featuring smart beat-syncing. Simply describe the desired tone—e.g., "Restrained," "Emotional," or "Documentary-style"—and the system matches suitable voiceovers and fonts to ensure a cohesive aesthetic.
- 💬 **Conversational Refinement**: Rapidly cut, swap, or resequence clips. Edit scripts and fine-tune visual details—including color, font, stroke, and position. All edits are performed exclusively via natural language prompts with immediate results.
- ⚡**Editing Skill Archiving**: Save your complete editing workflow as a custom Skill. Simply swap the media and apply the corresponding Skill to instantly replicate the style, enabling efficient batch creation.

## NEWS

* 🎬 **2026-04-02**: Added the **AI Transition Generation** feature, which automatically creates transition shots based on the ending frame of one clip, the opening frame of the next, and a natural-language description, making scene transitions smoother and the narrative more coherent.
* 🚀 **2026-03-22**: Introduced an **ASR-based rough cut skill for speech videos**, enabling automatic removal of filler words, disfluencies, and repeated sentences, with timestamp-aligned segmentation for cleaner and more efficient speech editing workflows.
* 🔥 **2026-03-12**: Integrated with **OpenClaw**, adding two OpenClaw Skills — `openstoryline-install` and `openstoryline-use` — covering the initial installation/first-run workflow and the actual usage workflow, respectively. Also added Skill usage instructions for **Claude Code**, making it easier for **Claude Code** to install and invoke the project in accordance with the repository guidelines.
* **2026-02-10**: FireRed-OpenStoryline was officially open-sourced.

> <sub>
> ⚠️ Note: AI transitions rely on third-party AIGC video generation services, and <b>the cost is relatively high</b>. Due to variations in source material quality, prompts, and model performance, the generated results are somewhat unpredictable. It is recommended to enable this feature only when needed.
> </sub>

## 🏗️ Architecture

<p align="center">
  <img src="https://raw.githubusercontent.com/FireRedTeam/fireredteam.github.io/main/demos/firered_openstoryline/pics/structure.jpg" alt="openstoryline architecture" width="800">
</p>

## ✨ Demo
<table align="center">
  <tr>
    <td align="center"><b>Zhongcao Style</b></td>
    <td align="center"><b>Humorous Style</b></td>
    <td align="center"><b>Product Picks</b></td>
    <td align="center"><b>Artistic Style</b></td>
  </tr>
  <tr>
    <td align="center"><video src="https://github.com/user-attachments/assets/28043813-1fda-4077-80d4-c6f540d7c7cb" width="220" /></td>
    <td align="center"><video src="https://github.com/user-attachments/assets/a1e33da2-a799-4398-a1bb-b25bb5143d7c" width="220" /></td>
    <td align="center"><video src="https://github.com/user-attachments/assets/444fd0fb-8824-4c25-b449-9309b0fcfd85" width="220" /></td>
    <td align="center"><video src="https://github.com/user-attachments/assets/2e69fa0d-b693-4d4f-b4d2-45146254f9e8" width="220" /></td>
  </tr>

  <tr>
    <td align="center"><b>Unboxing</b></td>
    <td align="center"><b>Talking Pet</b></td>
    <td align="center"><b>Travel Vlog</b></td>
    <td align="center"><b>Year-in

## installation

### 1. Clone repository
```
# If git is not installed, refer to the official website for installation: https://git-scm.com/install/
# Or manually download the code
git clone https://github.com/FireRedTeam/FireRed-OpenStoryline.git
cd FireRed-OpenStoryline
```

## configuration

Install Conda according to the official guide (Miniforge is recommended, it is suggested to check the option to automatically configure environment variables during installation): https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html


```
# Recommended python>=3.11
conda create -n storyline python=3.11
conda activate storyline
```

## requirements

- [MoviePy](https://github.com/Zulko/moviepy) - Video editing library
- [FFmpeg](https://ffmpeg.org/) - Multimedia framework
- [LangChain](https://www.langchain.com/) - A framework that provides pre-built Agents

## 📄 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## ⭐ Star History

<div align="center"> <p> <img width="800" src="https://api.star-history.com/svg?repos=FireRedTeam/FireRed-OpenStoryline&type=Date" alt="Star-history"> </p> </div>
