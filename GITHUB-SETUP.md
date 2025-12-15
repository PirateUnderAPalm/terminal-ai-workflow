# GitHub Integration Guide

## Current Status

✅ **SSH Keys**: Configured and tested
✅ **GitHub Connection**: Working
✅ **Infrastructure Repo**: Public at https://github.com/PirateUnderAPalm/terminal-ai-workflow
✅ **New Project Integration**: Automated

---

## How It Works

### Infrastructure Repository (Public)

**Repository**: https://github.com/PirateUnderAPalm/terminal-ai-workflow
**Visibility**: Public
**Contains**: Templates, scripts, automation, documentation

**To update the infrastructure**:
```bash
cd /data/ai-projects
git add .
git commit -m "Description of changes"
git push origin main
```

### Individual Project Repositories (Private by Default)

Each project you create with `new-project` can have its own private GitHub repository.

#### Automatic (with GitHub CLI)

If GitHub CLI is installed and authenticated:
```bash
new-project my-new-project
# Will prompt: "Create a private GitHub repository?"
# Answer 'y' and it automatically creates and pushes
```

#### Manual Method

If GitHub CLI is not installed:
```bash
# 1. Create project locally
new-project my-new-project
cd /data/ai-projects/active-projects/my-new-project

# 2. Create repo on GitHub
# Go to https://github.com/new
# Name: my-new-project
# Visibility: Private
# Do NOT initialize with README
# Click "Create repository"

# 3. Connect and push
git remote add origin git@github.com:PirateUnderAPalm/my-new-project.git
git push -u origin main
```

---

## Session-Closer Integration

The `session-closer` script commits locally. To push to GitHub:

**Option 1: Manual push after closing**
```bash
session-closer  # Creates local commit
git push        # Push to GitHub
```

**Option 2: Enhanced session-closer** (future)
We can modify `session-closer` to automatically push after committing.

---

## GitHub CLI Setup (Optional but Recommended)

GitHub CLI (`gh`) makes repo creation automatic.

### Install GitHub CLI

```bash
# Add GitHub CLI repository
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg

echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null

# Install
sudo apt update
sudo apt install gh

# Authenticate
gh auth login
# Choose: GitHub.com
# Choose: SSH
# Choose: Login with a web browser
# Follow prompts
```

Once installed, `new-project` will automatically offer to create GitHub repos.

---

## Repository Management

### Making a Private Repo Public

```bash
cd /data/ai-projects/active-projects/your-project

# With GitHub CLI
gh repo edit --visibility public

# Or on GitHub web: Settings → Danger Zone → Change visibility
```

### Creating Additional Remotes

```bash
# Add a backup remote
git remote add backup git@github.com:username/backup-repo.git

# Push to multiple remotes
git push origin main
git push backup main
```

### Checking Repository Status

```bash
# View remotes
git remote -v

# Check if pushed to GitHub
git status

# View commit history
git log --oneline
```

---

## Workflow Examples

### Example 1: Research Project with GitHub

```bash
# Create project
new-project coffee-research
# Answer 'y' to create GitHub repo

cd /data/ai-projects/active-projects/coffee-research

# Edit context
nano claude.md

# Work with AI
claude

# End session (creates commit)
session-closer

# Push to GitHub
git push
```

### Example 2: Private Work, Publish Later

```bash
# Create project without GitHub
new-project secret-project
# Answer 'n' to GitHub question

# Work privately for weeks
cd /data/ai-projects/active-projects/secret-project
claude
session-closer
# Repeat...

# Later: Ready to share
gh repo create secret-project --private --source=. --remote=origin
git push -u origin main

# Even later: Make it public
gh repo edit secret-project --visibility public
```

### Example 3: Collaborate with Others

```bash
# Create private repo
new-project team-project
# Answer 'y' to create GitHub repo

# Add collaborators on GitHub
# Settings → Collaborators → Add people

# They clone:
git clone git@github.com:PirateUnderAPalm/team-project.git

# Both of you work:
session-closer  # Local commit
git pull        # Get their changes
git push        # Share your changes
```

---

## Security Best Practices

### What NOT to Commit

✅ **Do commit**:
- Context files (claude.md, gemini.md)
- Research notes
- Code
- Documentation
- Session summaries

❌ **Never commit**:
- API keys (use environment variables)
- Passwords
- Private credentials
- `.env` files with secrets

**The template `.gitignore` already blocks**:
- `*.key`
- `*api_key*`
- `.env`

### Checking Before Push

```bash
# Review what will be pushed
git status
git diff

# Check for secrets
git diff | grep -i "api"
git diff | grep -i "password"
git diff | grep -i "secret"
```

---

## Backup Strategy

### Your Data is in Three Places

1. **Local**: `/data/ai-projects/`
2. **GitHub**: https://github.com/PirateUnderAPalm/*
3. **Git History**: Every commit preserved

### Full Backup

```bash
# Backup everything
tar -czf ai-projects-backup-$(date +%Y%m%d).tar.gz /data/ai-projects/

# Or rsync to another drive
rsync -av /data/ai-projects/ /backup/ai-projects/
```

---

## Troubleshooting

### "Permission denied (publickey)"

SSH key issue. Verify:
```bash
ssh -T git@github.com
# Should say: "Hi PirateUnderAPalm!"
```

If not:
```bash
# Check key is loaded
ssh-add -l

# Add key if needed
ssh-add ~/.ssh/id_ed25519
```

### "Repository not found"

Wrong username or repo name:
```bash
# Check remote
git remote -v

# Fix if wrong
git remote set-url origin git@github.com:PirateUnderAPalm/correct-name.git
```

### "Failed to push"

Not up to date:
```bash
# Pull first
git pull --rebase origin main

# Then push
git push
```

---

## Summary

**Infrastructure**: Public repo for templates/scripts
**Projects**: Private by default, you control visibility
**Automation**: `new-project` offers GitHub creation
**Workflow**: Work locally, commit with `session-closer`, push when ready

Your AI work is version-controlled, backed up, and shareable when you choose.

---

**GitHub Username**: PirateUnderAPalm
**Infrastructure**: https://github.com/PirateUnderAPalm/terminal-ai-workflow
**SSH Key**: Configured at ~/.ssh/id_ed25519
