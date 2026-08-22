# notlikeDev/CCPlugins

Best Claude Code framework that actually save time. Built by a dev tired of typing "please act like a senior engineer" in every conversation.

## installation

### Quick Install

**Mac/Linux:**
```bash
curl -sSL https://raw.githubusercontent.com/brennercruvinel/CCPlugins/main/install.sh | bash
```

**Windows/Cross-platform:**
```bash
python install.py
```

### Manual Install
```bash
git clone https://github.com/brennercruvinel/CCPlugins.git
cd CCPlugins
python install.py
```

### Uninstall
```bash
# Mac/Linux
./uninstall.sh

# Windows/Cross-platform
python uninstall.py
```

## tools

24 professional commands optimized for Claude Code CLI's native capabilities with enhanced validation and refinement phases.

### Development Workflow

```bash
/cleanproject                    # Remove debug artifacts with git safety
/commit                          # Smart conventional commits with analysis
/format                          # Auto-detect and apply project formatter
/scaffold feature-name           # Generate complete features from patterns
/test                            # Run tests with intelligent failure analysis
/implement url/path/feature      # Import and adapt code from any source with validation phase
/refactor                        # Intelligent code restructuring with validation & de-para mapping
```

### Code Quality & Security

```bash
/review                # Multi-agent analysis (security, performance, quality, architecture)
/security-scan         # Vulnerability analysis with extended thinking & remediation tracking
/predict-issues        # Proactive problem detection with timeline estimates
/remove-comments       # Clean obvious comments, preserve valuable docs
/fix-imports           # Repair broken imports after refactoring
/find-todos            # Locate and organize development tasks
/create-todos          # Add contextual TODO comments based on analysis results
/fix-todos             # Intelligently implement TODO fixes with context
```

### Advanced Analysis

```bash
/understand            # Analyze entire project architecture and patterns
/explain-like-senior   # Senior-level code explanations with context
/contributing          # Complete contribution readiness analysis
/make-it-pretty        # Improve readability without functional changes
```

### Session & Project Management

```bash
/session-start         # Begin documented sessions with CLAUDE.md integration
/session-end           # Summarize and preserve session context
/docs                  # Smart documentation management and updates
/todos-to-issues       # Convert code TODOs to GitHub issues
/undo                  # Safe rollback with git checkpoint restore
```

## features

### 🔍 Validation & Refinement
Complex commands now include validation phases to ensure completeness:
```bash
/refactor validate   # Find remaining old patterns, verify 100% migration
/implement validate  # Check integration completeness, find loose ends
```

### Extended Thinking
Advanced analysis for complex scenarios:
- **Refactoring**: Deep architectural analysis for large-scale changes
- **Security**: Sophisticated vulnerability detection with chain analysis

### Pragmatic Command Integration
Natural workflow suggestions without over-engineering:
- Suggests `/test` after major changes
- Recommends `/commit` at logical checkpoints
- Maintains user control, no automatic execution

## Real World Example

### Before `/cleanproject`:
```
src/
├── UserService.js
├── UserService.test.js
├── UserService_backup.js    # Old version
├── debug.log               # Debug output
├── test_temp.js           # Temporary test
└── notes.txt              # Dev notes
```

### After `/cleanproject`:
```
src/
├── UserService.js          # Clean production code
└── UserService.test.js     # Actual tests preserved
```

## 🔧 How It Works

### High-Level Architecture

CCPlugins transforms Claude Code CLI into an intelligent development assistant through a sophisticated yet elegant architecture:

```
Developer → /command → Claude Code CLI → Command Definition → Intelligent Execution
    ↑                                                                       ↓
    ←←←←←←←←←←←←←←←←← Clear Feedback & Results ←←←←←←←←←←←←←←←←←←←
```

### Execution Flow

When you type a command:

1. **Command Loading**: Claude reads the markdown definition from `~/.claude/commands/`
2. **Context Analysis**: Analyzes your project structure, technology stack, and current state
3. **Intelligent Planning**: Creates execution strategy based on your specific situation
4. **Safe Execution**: Performs actions with automatic checkpoints and validation
5. **Clear Feedback**: Provides results, next steps, and any warnings

### Core Architecture Components

**Intelligent Instructions**
- First-person conversational design activates collaborative reasoning
- Strategic thinking sections (`<think>`) for complex decision-making
- Context-aware adaptations without hardcoded assumptions

**Native Tool Integration**
- **Grep**: Lightning-fast pattern matching across codebases
- **Glob**: Intelligent file discovery and project mapping
- **Read**: Content analysis with full context understanding
- **Write**: Safe file modifications with automatic backups
- **TodoWrite**: Progress tracking and task management
- **Task**: Sub-agent orchestration for specialized analysis

**Safety-First Design**
- Automatic git checkpoints before destructive operations
- Session persistence for cross-context continuity
- Rollback capabilities with clear recovery paths
- No AI attribution in commits or generated content

**Universal Compatibility**
- Framework-agnostic with intelligent auto-detection
- Cross-platform support (Windows, Linux, macOS)
- Works with any programming language or stack
- Adapts to your project's conventions and patterns

### Advanced Features

**Session Continuity**
Commands like `/implement` and `/refactor` maintain state across Claude sessions:
```
# Each command creates its own folder in project root:
refactor/                  # Created by /refactor command
├── plan.md               # Refactoring roadmap
└── state.json            # Completed transformations

implement/                 # Created by /implement command
├── plan.md               # Implementation progress
└── state.json            # Session state and decisions

fix-imports/              # Created by /fix-imports command
├── plan.md               # Import fixes plan
└── state.json            # Resolution progress

security-scan/            # Created by /security-scan command
├── plan.md               # Vulnerabilities and fixes
└── state.json            # Remediation progress

scaffold/                 # Created by /scaffol

## requirements

- Claude Code CLI
- Python 3.6+ (for installer)
- Git (for version control commands)
