# Quick Start Guide

## 5-Minute Setup

### 1. Configure Git
```bash
setup-git
```

### 2. Set Gemini API Key (Optional)
```bash
# Get your key: https://makersuite.google.com/app/apikey
echo 'export GEMINI_API_KEY="your-key-here"' >> ~/.bashrc
source ~/.bashrc
```

### 3. Create First Project
```bash
new-project my-first-project
cd /data/ai-projects/active-projects/my-first-project
```

### 4. Start Working
```bash
# Use Claude (already working!)
claude

# Or Gemini (if API key set)
gemini

# Or local models (free, private)
opencode -m deepseek-coder:latest
```

---

## Essential Commands

| Command | Purpose |
|---------|---------|
| `new-project <name>` | Create new AI project |
| `claude` | Start Claude Code session |
| `gemini` | Start Gemini session |
| `opencode` | Use local Ollama models |
| `session-closer` | End session + commit |
| `ai-agent critic` | Launch critic agent |
| `setup-git` | Configure Git |

---

## Your First Workflow

1. **Create project**
   ```bash
   new-project coffee-research
   cd /data/ai-projects/active-projects/coffee-research
   ```

2. **Edit context**
   ```bash
   nano claude.md  # Set your objectives
   ```

3. **Start session**
   ```bash
   claude  # Auto-loads claude.md context
   ```

4. **Work** - AI reads/writes files directly

5. **Close session**
   ```bash
   session-closer  # Summary + commit
   ```

6. **Done!** Context is saved, Git has history

---

## File Context Pattern

Each project has these context files:

- `claude.md` - Claude's instructions
- `gemini.md` - Gemini's instructions
- `agents.md` - Agent roles
- `README.md` - Project overview

**AI tools auto-load these on startup!**

Update them as your project evolves.

---

## Available Local Models

Run `opencode --list` to see all models.

Popular choices:
- `deepseek-coder:latest` - Best for coding
- `mixtral:latest` - General purpose, powerful
- `mistral:latest` - Fast and efficient
- `wizardcoder:latest` - Code generation

Use: `opencode -m model-name`

---

## Tips

✅ **DO**:
- Update context files regularly
- Commit after meaningful work
- Use agents for specialized tasks
- Keep main context lean

❌ **DON'T**:
- Let context files get stale
- Skip commits (Git is mandatory!)
- Re-explain context each session
- Use browser chats for project work

---

## Next Steps

Read the full manual:
```bash
cat /data/ai-projects/README.md
```

Or just start building!
