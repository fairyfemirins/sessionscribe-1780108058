#!/usr/bin/env python3

import click
import pyte
import time
import os
import re
from datetime import datetime
from pathlib import Path

# Global state
screen = pyte.Screen(80, 24)
stream = pyte.Stream()
stream.attach(screen)
recording = False
session_log = []
sensitive_patterns = [
    r"\bpassword\b.*",
    r"\bapi[_-]?key\b.*",
    r"\bsecret\b.*",
    r"\btoken\b.*"
]

def redact_sensitive(text):
    """Redact sensitive data from text."""
    for pattern in sensitive_patterns:
        text = re.sub(pattern, "[REDACTED]", text, flags=re.IGNORECASE)
    return text

@click.group()
def cli():
    """SessionScribe: Terminal Session Auto-Documenter"""
    pass

@cli.command()
@click.option("--exclude-sensitive", is_flag=True, help="Exclude sensitive data from the output.")
def start(exclude_sensitive):
    """Start recording the terminal session."""
    global recording, session_log
    recording = True
    session_log = []
    click.echo("SessionScribe: Recording started. Press Ctrl+D or type 'exit' to stop.")
    
    # Simulate terminal input (for demo purposes)
    try:
        while recording:
            line = input()
            if line.strip() == "exit":
                break
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            processed_line = redact_sensitive(line) if exclude_sensitive else line
            session_log.append((timestamp, processed_line))
            stream.feed(line + "\n")
    except EOFError:
        pass

@cli.command()
def stop():
    """Stop recording and generate SESSION.md."""
    global recording
    recording = False
    
    if not session_log:
        click.echo("SessionScribe: No session data recorded.")
        return
    
    # Generate Markdown
    md_content = f"# Terminal Session: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    for timestamp, line in session_log:
        if line.strip().startswith("#"):
            md_content += f"\n## {line.strip()[1:].strip()}\n"
        else:
            md_content += f"**Command:** `{line.strip()}`\n\n**Output:**\n```\n"
            # Simulate output (for demo purposes)
            md_content += f"Output for '{line.strip()}'\n```\n\n"
    
    # Write to file
    output_path = Path("SESSION.md")
    output_path.write_text(md_content)
    click.echo(f"SessionScribe: Session saved to {output_path}")

if __name__ == "__main__":
    cli()