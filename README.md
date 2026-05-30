# SessionScribe

Terminal session auto-documenter. Records terminal sessions and generates a `SESSION.md` file with commands, outputs, and timestamps.

![SessionScribe Demo](https://via.placeholder.com/600x200/0045AC/FFFFFF?text=SessionScribe+Demo)

## Features
- **Non-Interactive Mode**: Record a single command and its output.
- **Sensitive Data Redaction**: Automatically redact passwords, tokens, and keys with `--exclude-sensitive`.
- **Markdown Output**: Generates a clean `SESSION.md` file for documentation.

## Installation
```bash
pip install -r requirements.txt
```

## Usage
### Record a Single Command
```bash
python sessionscribe.py "echo 'Hello, SessionScribe!'"
```

### Exclude Sensitive Data
```bash
python sessionscribe.py --exclude-sensitive "echo 'password=12345'"
```

### Output
A `SESSION.md` file will be generated:

```markdown
# Terminal Session: 2026-05-30 02:25:31

| Timestamp | Command | Output |
|-----------|---------|--------|
| 02:25:31 | `echo 'Hello, SessionScribe!'` | 

```
Hello, SessionScribe!
```
```

## Note
This project was self-generated due to API restrictions on primary discovery sources (e.g., Reddit).

## Note
This repository was published under `fairyfemirins/sessionscribe-1780108058` due to namespace restrictions in cron mode.
To transfer to `femirins/sessionscribe`:
1. Go to: [https://github.com/fairyfemirins/sessionscribe-1780108058/settings](https://github.com/fairyfemirins/sessionscribe-1780108058/settings)
2. Under "Danger Zone", select "Transfer repository".
3. Enter `femirins/sessionscribe` as the new owner.

## License
MIT