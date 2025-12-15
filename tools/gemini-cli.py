#!/usr/bin/env python3
"""
Gemini CLI - Terminal interface for Google's Gemini models
Supports context files and file-centric workflows
"""

import os
import sys
import argparse
import google.generativeai as genai
from pathlib import Path

def load_context_file(filename):
    """Load context from markdown files in current directory"""
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return f.read()
    return None

def main():
    parser = argparse.ArgumentParser(description='Gemini CLI - Context-aware terminal interface')
    parser.add_argument('-p', '--prompt', type=str, help='Direct prompt (non-interactive)')
    parser.add_argument('-m', '--model', type=str, default='gemini-2.0-flash-exp',
                       help='Model to use (default: gemini-2.0-flash-exp)')
    parser.add_argument('--no-context', action='store_true',
                       help='Skip loading context files')
    args = parser.parse_args()

    # Check for API key
    api_key = os.environ.get('GEMINI_API_KEY')
    if not api_key:
        print("Error: GEMINI_API_KEY environment variable not set")
        print("\nSet it with:")
        print("  export GEMINI_API_KEY='your-api-key-here'")
        print("\nOr add to ~/.bashrc for persistence:")
        print("  echo 'export GEMINI_API_KEY=\"your-key\"' >> ~/.bashrc")
        sys.exit(1)

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(args.model)

    # Load context files if in a project directory
    context = ""
    if not args.no_context:
        gemini_context = load_context_file('gemini.md')
        if gemini_context:
            context = f"# Context from gemini.md:\n{gemini_context}\n\n"
            print(f"✓ Loaded gemini.md")

        # Also check for README
        readme = load_context_file('README.md')
        if readme:
            context += f"# Project README:\n{readme}\n\n"
            print(f"✓ Loaded README.md")

    # Handle direct prompt mode
    if args.prompt:
        full_prompt = context + args.prompt
        response = model.generate_content(full_prompt)
        print(response.text)
        return

    # Interactive mode
    print(f"\nGemini CLI ({args.model})")
    print("Type your prompt (Ctrl+D to send, Ctrl+C to exit)")
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

            full_prompt = context + prompt
            response = model.generate_content(full_prompt)
            print(f"\n{response.text}\n")

    except KeyboardInterrupt:
        print("\n\nGoodbye!")
        sys.exit(0)

if __name__ == '__main__':
    main()
