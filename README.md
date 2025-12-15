# Terminal-Native AI Workflow System
## Context-First, File-Centric, Multi-Agent Operations

**Location**: `/data/ai-projects`

This system implements the terminal-native AI workflow philosophy:
- Context lives in files, not chats
- Projects are directories
- AI sessions are disposable
- State is persistent
- Agents protect context
- Git tracks thinking

---

## Quick Start

### 1. First-Time Setup

```bash
# Configure Git (if not already done)
setup-git

# Set up API keys (see API Keys section below)
export GEMINI_API_KEY="your-key-here"
# Add to ~/.bashrc for persistence
```

### 2. Create a New Project

```bash
# Create a new AI project
new-project my-research-project

# Navigate to it
cd /data/ai-projects/active-projects/my-research-project
```

### 3. Start Working

```bash
# Use Claude Code (cloud)
claude

# Use Gemini (cloud)
gemini

# Use local models via Ollama
opencode -m deepseek-coder:latest

# List available local models
opencode --list
```

All tools automatically load context from:
- `claude.md` - Claude-specific context
- `gemini.md` - Gemini-specific context
- `agents.md` - Agent definitions
- `README.md` - Project overview

---

## Available Tools

### Cloud-Based

#### Claude Code (You're using it now!)
```bash
claude
```
- Best for: Complex reasoning, planning, multi-step tasks
- Uses Claude Sonnet/Opus models
- Built-in agent support
- Already installed

#### Gemini CLI
```bash
gemini -m gemini-2.0-flash-exp
gemini -p "Quick question here"
```
- Best for: Fast iterations, research, cost-effective tasks
- Uses Google's Gemini models
- Requires: `GEMINI_API_KEY` environment variable

### Local Models

#### OpenCode (Ollama wrapper)
```bash
opencode                           # Interactive mode
opencode -m deepseek-coder:latest  # Specify model
opencode -p "Code review this"     # Direct prompt
opencode --list                    # Show available models
```
- Best for: Privacy, offline work, zero marginal cost
- Uses your local Ollama models
- Available models: deepseek-coder, mixtral, wizard-coder, etc.
- No API key required

---

## Project Structure

Every project created with `new-project` has:

```
project-name/
├── README.md              # Human overview
├── gemini.md              # Gemini context file
├── claude.md              # Claude context file
├── agents.md              # Agent role definitions
├── session-summary.md     # Rolling session log
├── decisions.md           # Decision history
├── research/
│   ├── sources.md         # Reference tracking
│   └── notes.md           # Research findings
├── output/
│   ├── drafts/            # Work in progress
│   └── finals/            # Completed deliverables
└── .git/                  # Version control
```

---

## Workflow Patterns

### Daily Loop

1. **Enter project directory**
   ```bash
   cd /data/ai-projects/active-projects/your-project
   ```

2. **Start AI tool** (auto-loads context)
   ```bash
   claude  # or gemini, or opencode
   ```

3. **Work on tasks**
   - Tool reads context from .md files
   - You guide the work
   - AI updates files directly

4. **End session**
   ```bash
   session-closer  # Interactive summary + Git commit
   ```

5. **Repeat**

### Using Agents

Agents give you fresh context windows for specialized tasks:

```bash
# Launch a brutal critic
ai-agent critic "Review my latest draft"

# Launch a researcher
ai-agent researcher "Find sources on quantum computing"

# Launch fact checker
ai-agent fact-checker "Verify claims in output/draft.md"
```

Or manually in Claude Code:
```bash
claude
# Then use Claude's built-in /agents command
```

### Context File Pattern

Before each session, update your context files:

**claude.md / gemini.md**:
- Current objectives
- Phase of work
- Open questions
- Quality standards

The AI loads these automatically and operates within those constraints.

---

## Automation Scripts

### `new-project <name>`
Creates a new project from template with:
- Full directory structure
- Pre-configured context files
- Git initialization
- Initial commit

### `session-closer`
Interactive end-of-session tool:
- Prompts for summary
- Updates session-summary.md
- Syncs context files
- Commits changes with meaningful message

### `ai-agent <type> [task]`
Quick launcher for specialized agents:
- `critic` - Brutal code/content review
- `researcher` - Deep research tasks
- `fact-checker` - Verify claims

### `setup-git`
One-time Git configuration for AI workflows

---

## API Keys Setup

### Gemini
```bash
# Get your API key from: https://makersuite.google.com/app/apikey
export GEMINI_API_KEY="your-key-here"

# Make it permanent
echo 'export GEMINI_API_KEY="your-key-here"' >> ~/.bashrc
source ~/.bashrc
```

### Claude Code
Claude Code uses Anthropic's API. If not already configured:
```bash
# Check Claude Code documentation
claude --help
```

---

## Available Local Models (via Ollama)

You have 20 models installed:

**Coding Specialists**:
- `deepseek-coder:latest` - Strong code generation
- `wizardcoder:latest` - Code completion
- `starcoder:latest` - Multi-language coding
- `sqlcoder:latest` - SQL specialist

**General Purpose**:
- `mixtral:latest` - Large, capable model
- `mistral:latest` - Fast, efficient
- `dolphin-mixtral:latest` - Uncensored reasoning
- `llama2:latest` - General tasks

**Specialized**:
- `wizard-math:latest` - Mathematics
- `yarn-mistral:latest` - Long context

Use with: `opencode -m model-name:latest`

---

## Multi-Tool Workflow Example

```bash
# Research phase with Gemini (fast, cheap)
cd /data/ai-projects/active-projects/blog-post
gemini -p "Research top 10 coffee brewing methods and write to research/methods.md"

# Planning with Claude (deep reasoning)
claude  # Opens interactive session
# Claude reads research, creates outline

# Code generation with local model (private, free)
opencode -m deepseek-coder:latest -p "Generate Python script for data analysis"

# Critical review with agent
ai-agent critic "Review output/draft.md"

# Close session
session-closer
```

Each tool works on the **same files**. Context is shared. No re-explaining.

---

## Integration with n8n (Future)

Your self-hosted n8n server can trigger AI workflows:

Potential patterns:
- Webhook receives data → writes to project → triggers AI analysis
- Scheduled n8n workflow → runs `gemini -p` → commits results
- n8n monitors Git → triggers on commits → posts to Slack

*Note: Not yet implemented - infrastructure ready*

---

## Best Practices

### Context Hygiene
- Keep context files concise
- Update them continuously
- Clear out stale information
- Use agents for one-off tasks (keeps main context clean)

### Git Discipline
- Commit after each meaningful change
- Use descriptive commit messages
- Session-closer helps with this

### Tool Selection
- **Claude**: Complex reasoning, architecture, planning
- **Gemini**: Research, iterations, cost-sensitive tasks
- **OpenCode/Ollama**: Privacy-sensitive, offline, experimental

### File Ownership
- **You own the files**
- AI tools are disposable
- Context is persistent
- Never trapped in a chat history

---

## Troubleshooting

### Scripts not found
```bash
# Add to PATH if missing
export PATH="/data/ai-projects/scripts:$PATH"
echo 'export PATH="/data/ai-projects/scripts:$PATH"' >> ~/.bashrc
```

### API key errors
```bash
# Verify environment variables
echo $GEMINI_API_KEY
# Should show your key, not blank
```

### Git not configured
```bash
setup-git  # Run the setup script
```

### Ollama not responding
```bash
# Check service status
systemctl status ollama

# Restart if needed
sudo systemctl restart ollama
```

---

## Directory Reference

```
/data/ai-projects/
├── active-projects/       # Your AI projects live here
├── templates/             # Project templates
│   └── project-template/  # Standard project structure
├── scripts/               # Automation scripts (in PATH)
│   ├── new-project        # Project scaffolding
│   ├── session-closer     # End-of-session tool
│   ├── ai-agent           # Agent launcher
│   ├── setup-git          # Git configuration
│   ├── gemini             # Gemini CLI wrapper
│   └── opencode           # Ollama CLI wrapper
└── tools/                 # Tool implementations
    ├── gemini-cli.py      # Gemini Python implementation
    └── ollama-cli.py      # Ollama Python implementation
```

---

## Next Steps

1. **Run first-time setup**
   ```bash
   setup-git  # Configure Git if needed
   ```

2. **Set API keys**
   ```bash
   # For Gemini (get key from https://makersuite.google.com/)
   echo 'export GEMINI_API_KEY="your-key"' >> ~/.bashrc
   source ~/.bashrc
   ```

3. **Create your first project**
   ```bash
   new-project test-project
   cd /data/ai-projects/active-projects/test-project
   ```

4. **Start experimenting**
   ```bash
   # Try each tool
   claude
   gemini
   opencode
   ```

5. **Develop your workflow**
   - Experiment with agents
   - Customize context files
   - Build your own patterns

---

## Philosophy Recap

> The AI is not your brain.
> It is your operating system extension.

- **Context in files** - Persistent, version-controlled, tool-agnostic
- **Sessions are disposable** - Restart anytime, context survives
- **Git tracks thinking** - Your decisions are code
- **Multi-tool by design** - Switch models at will

**You own your context. You control your workflows.**

---

## Support & Resources

- This system: `/data/ai-projects/`
- Templates: `/data/ai-projects/templates/`
- Scripts source: `/data/ai-projects/scripts/`

For issues or enhancements, modify the scripts directly.
They're yours to customize.

---

**System installed**: $(date +%Y-%m-%d)
**Last updated**: $(date +%Y-%m-%d)
