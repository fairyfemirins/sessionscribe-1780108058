#!/usr/bin/env python3
"""
SessionScribe: Terminal session auto-documenter.
Records terminal sessions and generates a SESSION.md file with commands, outputs, and timestamps.

Usage:
    python3 sessionscribe.py --output SESSION.md
    python3 sessionscribe.py --exclude-sensitive --output SESSION.md
"""

import os
import time
import click
import pyte
import markdown
from datetime import datetime

class TerminalRecorder:
    def __init__(self, exclude_sensitive=False):
        self.screen = pyte.Screen(80, 24)
        self.stream = pyte.ByteStream(self.screen)
        self.exclude_sensitive = exclude_sensitive
        self.commands = []
        self.current_command = ""
        self.sensitive_keywords = ["password", "token", "secret", "api_key"]

    def feed(self, data):
        """Feed terminal data to the recorder."""
        self.stream.feed(data)
        self._process_screen()

    def _process_screen(self):
        """Process the screen state and extract commands/outputs."""
        lines = self.screen.display
        for line in lines:
            line = line.rstrip()
            if line.endswith("$") or line.endswith("#"):
                # New prompt detected
                if self.current_command:
                    self.commands.append({
                        "command": self.current_command,
                        "output": "",
                        "timestamp": datetime.now().isoformat()
                    })
                    self.current_command = ""
            elif line and not line.isspace():
                if self.commands:
                    # Append to the last command's output
                    if self.exclude_sensitive:
                        for keyword in self.sensitive_keywords:
                            if keyword in line.lower():
                                line = "[REDACTED]"
                                break
                    self.commands[-1]["output"] += line + "\n"
                else:
                    # Start a new command
                    self.current_command += line + "\n"

    def generate_markdown(self):
        """Generate Markdown from recorded commands."""
        md_content = "# Terminal Session\n\n"
        md_content += f"**Recorded at:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        for cmd in self.commands:
            md_content += f"## Command\n```bash\n{cmd['command'].strip()}\n```\n"
            md_content += f"**Timestamp:** {cmd['timestamp']}\n\n"
            if cmd["output"].strip():
                md_content += "### Output\n```\n"
                md_content += cmd["output"].strip() + "\n"
                md_content += "```\n\n"
            md_content += "---\n"
        return md_content

@click.command()
@click.option("--exclude-sensitive", is_flag=True, help="Exclude sensitive data from output.")
@click.option("--output", default="SESSION.md", help="Output Markdown file.")
@click.option("--record", is_flag=True, help="Start recording terminal session.")
def cli(exclude_sensitive, output, record):
    """SessionScribe: Terminal session auto-documenter."""
    recorder = TerminalRecorder(exclude_sensitive=exclude_sensitive)
    
    if record:
        click.echo("Recording terminal session... Press Ctrl+D to stop.")
        try:
            while True:
                data = os.read(0, 1024)
                recorder.feed(data)
        except (EOFError, KeyboardInterrupt):
            pass
        
        md_content = recorder.generate_markdown()
        with open(output, "w") as f:
            f.write(md_content)
        click.echo(f"Session recorded and saved to {output}")
    else:
        click.echo("Use --record to start recording.")

if __name__ == "__main__":
    cli()