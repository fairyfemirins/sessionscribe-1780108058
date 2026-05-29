# SessionScribe

**Terminal Session Auto-Documenter**

Records terminal sessions and generates a `SESSION.md` file with commands, outputs, and timestamps. Supports `--exclude-sensitive` flag to redact sensitive data.

## Features
- Records terminal sessions in real-time.
- Generates a `SESSION.md` file with commands, outputs, and timestamps.
- Supports `--exclude-sensitive` flag to redact sensitive data (e.g., passwords, API keys).
- Lightweight and dependency-free (except for `click`, `pyte`, and `markdown`).

## Installation
```bash
pip install sessionscribe
```

## Usage
```bash
# Start recording
sessionscribe start

# Stop recording and generate SESSION.md
sessionscribe stop

# Exclude sensitive data
sessionscribe start --exclude-sensitive
```

## Output Example
```markdown
# Terminal Session: 2026-05-29 20:00:00

## Command: ls -la
```
-rw-r--r--  1 user  staff   123 May 29 19:59 README.md

## Command: echo "Hello, World!"
Hello, World!
```

## License
MIT