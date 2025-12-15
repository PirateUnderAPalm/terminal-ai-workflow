#!/usr/bin/env python3
"""
Ollama CLI - Context-aware terminal interface for local models
Supports the file-centric workflow with gemini.md, claude.md, etc.
"""

import os
import sys
import argparse
import subprocess
import json
from pathlib import Path

def load_context_file(filename):
    """Load context from markdown files in current directory"""
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return f.read()
    return None

def list_models():
    """List available Ollama models"""
    result = subprocess.run(['ollama', 'list'], capture_output=True, text=True)
    return result.stdout

def chat_with_ollama(model, prompt, system_prompt=None):
    """Send a prompt to Ollama"""
    messages = []

    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})

    messages.append({"role": "user", "content": prompt})

    cmd = ['ollama', 'run', model]

    # Send prompt via stdin
    process = subprocess.Popen(
        cmd,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    stdout, stderr = process.communicate(input=prompt)
    return stdout

def main():
    parser = argparse.ArgumentParser(description='Ollama CLI - Context-aware local model interface')
    parser.add_argument('-p', '--prompt', type=str, help='Direct prompt (non-interactive)')
    parser.add_argument('-m', '--model', type=str, default='deepseek-coder:latest',
                       help='Model to use (default: deepseek-coder:latest)')
    parser.add_argument('--list', action='store_true',
                       help='List available models')
    parser.add_argument('--no-context', action='store_true',
                       help='Skip loading context files')
    args = parser.parse_args()

    # List models and exit
    if args.list:
        print(list_models())
        return

    # Load context files if in a project directory
    context = ""
    system_context = ""

    if not args.no_context:
        # Try loading different context files
        for ctx_file in ['claude.md', 'gemini.md', 'agents.md']:
            content = load_context_file(ctx_file)
            if content:
                context += f"# Context from {ctx_file}:\n{content}\n\n"
                print(f"✓ Loaded {ctx_file}")

        # Also check README
        readme = load_context_file('README.md')
        if readme:
            context += f"# Project README:\n{readme}\n\n"
            print(f"✓ Loaded README.md")

        if context:
            system_context = f"You are working in a project directory with the following context:\n\n{context}"

    # Handle direct prompt mode
    if args.prompt:
        full_prompt = args.prompt
        if context:
            full_prompt = f"{context}\n\nUser request: {args.prompt}"

        print(f"\nUsing model: {args.model}")
        print(f"Sending prompt to Ollama...\n")

        # Use direct ollama run command for better streaming
        cmd = ['ollama', 'run', args.model, full_prompt]
        subprocess.run(cmd)
        return

    # Interactive mode
    print(f"\nOllama CLI ({args.model})")
    print(f"Type your prompt (Ctrl+D to send, Ctrl+C to exit)")
    if context:
        print("Context loaded from project files\n")

    try:
        while True:
            print("\n> ", end='')
            lines = []
            try:
                while True:
                    line = input()
                    lines.append(line)
            except EOFError:
                pass

            prompt = '\n'.join(lines)
            if not prompt.strip():
                continue

            full_prompt = prompt
            if context:
                full_prompt = f"{context}\n\nUser request: {prompt}"

            # Use direct ollama command for streaming output
            cmd = ['ollama', 'run', args.model, full_prompt]
            subprocess.run(cmd)

    except KeyboardInterrupt:
        print("\n\nGoodbye!")
        sys.exit(0)

if __name__ == '__main__':
    main()
