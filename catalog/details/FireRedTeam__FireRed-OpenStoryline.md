# FireRedTeam/FireRed-OpenStoryline

FireRed-OpenStoryline is an AI video editing agent that transforms manual editing into intention-driven directing through natural language interaction, LLM-powered planning, and precise tool orchestra

## features

- 🌐 **Smart Media Search & Organization**: Automatically searches online and downloads images and video clips that match your requirements. Performs clip segmentation and content understanding based on your thematic media.
- ✍️ **Intelligent Script Generation**: Combines user themes, visual understanding, and emotion recognition to automatically construct storylines and context-aware narration. Features built-in Few-shot style transfer capabilities, allowing users to define specific copy styles (e.g., product reviews, casual vlogs) via reference text, achieving precise replication of tone, rhythm, and sentence structure.
- 🎵 **Intelligent Music, Voiceover & Font Recommendations**: Supports personal playlist imports and auto-recommends BGM based on content and mood, featuring smart beat-syncing. Simply describe the desired tone—e.g., "Restrained," "Emotional," or "Documentary-style"—and the system matches suitable voiceovers and fonts to ensure a cohesive aesthetic.
- 💬 **Conversational Refinement**: Rapidly cut, swap, or resequence clips. Edit scripts and fine-tune visual details—including color, font, stroke, and position. All edits are performed exclusively via natural language prompts with immediate results.
- ⚡**Editing Skill Archiving**: Save your complete editing workflow as a custom Skill. Simply swap the media and apply the corresponding Skill to instantly replicate the style, enabling efficient batch creation.

## configuration

Install Conda according to the official guide (Miniforge is recommended, it is suggested to check the option to automatically configure environment variables during installation): https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html


```

## installation

#### 3.1 Automatic Installation (Linux and macOS only)
```
sh build_env.sh
```
#### 3.2 Manual Installation
##### A. MacOS or Linux
  - Step 1: Install wget (if not already installed)

    ```
    # MacOS: If you haven't installed Homebrew yet, please install it first: https://brew.sh/
    brew install wget
    
    # Ubuntu/Debian
    sudo apt-get install wget
    
    # CentOS
    sudo yum install wget
    ```
  - Step 2: Download Resources

    ```bash
    chmod +x download.sh
    ./download.sh
    ```
  
  - Step 3: Install Dependencies

    ```bash
    pip install -r requirements.txt
    ```
    If you plan to use `storyline.local_asr`, make sure `torchaudio` is installed in the same environment.

##### B. Windows

  - Step 1: Prepare Directory: Create a new directory named `resource` in the project root directory.

  - Step 2: Download and Extract:

    *   [Download Models (models.zip)](https://image-url-2-feature-1251524319.cos.ap-shanghai.myqcloud.com/openstoryline/models.zip) -> Extract to the `.storyline` directory.

    *   [Download Resources (resource.zip)](https://image-url-2-feature-1251524319.cos.ap-shanghai.myqcloud.com/openstoryline/resource.zip) -> Extract to the `resource` directory.
  - Step 3:  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
    If you plan to use `storyline.local_asr`, make sure `torchaudio` is installed in the same environment.

## requirements

- [MoviePy](https://github.com/Zulko/moviepy) - Video editing library
- [FFmpeg](https://ffmpeg.org/) - Multimedia framework
- [LangChain](https://www.langchain.com/) - A framework that provides pre-built Agents
