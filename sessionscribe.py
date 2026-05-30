#!/usr/bin/env python3
"""
SessionScribe: Terminal session auto-documenter.
Records terminal sessions and generates a SESSION.md file with commands, outputs, and timestamps.
"""

import os
import time
import click
import subprocess
import pyte
from datetime import datetime
import re

class SessionRecorder:
    def __init__(self, output_file="SESSION.md", exclude_sensitive=False):
        self.output_file = output_file
        self.exclude_sensitive = exclude_sensitive
        self.screen = pyte.Screen(80, 24)
        self.stream = pyte.Stream(self.screen)
        self.session_start = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.commands = []
        self.current_command = ""
        self.sensitive_patterns = [
            r"\b(password|token|key|secret)\s*=\s*[^\s]+",
            r"\b(export\s+)?(AWS_ACCESS_KEY_ID|AWS_SECRET_ACCESS_KEY|GITHUB_TOKEN)\s*=\s*[^\s]+",
            r"\b(curl|wget|http)\s+.*--header\s+.*Authorization:\s*[^\s]+"
        ]

    def _redact_sensitive(self, text):
        if not self.exclude_sensitive:
            return text
        for pattern in self.sensitive_patterns:
            text = re.sub(pattern, "[REDACTED]", text, flags=re.IGNORECASE)
        return text

    def _write_header(self):
        with open(self.output_file, "w") as f:
            f.write(f"# Terminal Session: {self.session_start}\n\n")
            f.write("| Timestamp | Command | Output |\n")
            f.write("|-----------|---------|--------|\n")

    def _write_command(self, command, output):
        timestamp = datetime.now().strftime("%H:%M:%S")
        command = self._redact_sensitive(command)
        output = self._redact_sensitive(output)
        with open(self.output_file, "a") as f:
            f.write(f"| {timestamp} | `{command}` | \n\n")
            f.write(f"```\n{output}```\n\n")

    def record(self, command, output):
        if not self.commands:
            self._write_header()
        self.commands.append((command, output))
        self._write_command(command, output)

    def start_interactive(self):
        import pty
        import subprocess
        import select
        import termios
        import tty

        def read(fd):
            data = os.read(fd, 1024)
            self.stream.feed(data.decode())
            return data

        def write(fd, data):
            os.write(fd, data)

        def main():
            (child_pid, fd) = pty.fork()
            if child_pid == 0:
                subprocess.run(os.environ.get("SHELL", "/bin/bash"))
            else:
                old_settings = termios.tcgetattr(fd)
                try:
                    tty.setraw(fd)
                    while True:
                        r, _, _ = select.select([fd], [], [], 0.1)
                        if fd in r:
                            data = read(fd)
                            if data == b'exit\r\n':
                                break
                        time.sleep(0.1)
                finally:
                    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

        main()

@click.command()
@click.option("--output", "-o", default="SESSION.md", help="Output Markdown file.")
@click.option("--exclude-sensitive", "-s", is_flag=True, help="Exclude sensitive data (passwords, tokens).")
@click.option("--interactive", "-i", is_flag=True, help="Start an interactive terminal session.")
@click.argument("command", required=False, nargs=-1)
def cli(output, exclude_sensitive, interactive, command):
    recorder = SessionRecorder(output, exclude_sensitive)
    if interactive:
        recorder.start_interactive()
    else:
        import sys
        if not command:
            click.echo("Usage: sessionscribe --command 'your_command'")
            sys.exit(1)
        cmd_str = " ".join(command)
        output = subprocess.run(cmd_str, shell=True, capture_output=True, text=True).stdout
        recorder.record(cmd_str, output)

if __name__ == "__main__":
    cli()