# SessionScribe

**Terminal session auto-documenter.**

Records terminal sessions and generates a `SESSION.md` file with commands, outputs, and timestamps.

## Features
- Records terminal sessions in real-time.
- Generates Markdown documentation (`SESSION.md`).
- Excludes sensitive data (e.g., passwords, tokens) with `--exclude-sensitive`.
- Lightweight and dependency-minimal.

## Installation
```bash
pip install --break-system-packages click pyte markdown
git clone https://github.com/femirins/sessionscribe.git
cd sessionscribe
```

## Usage
```bash
# Start recording
python3 sessionscribe.py --record --output SESSION.md

# Exclude sensitive data
python3 sessionscribe.py --record --exclude-sensitive --output SESSION.md
```

## Limitations
- **Python Environment**: Requires `pyte` to be installed and detectable in the Python path. If you encounter `ModuleNotFoundError: No module named 'pyte'`, ensure it is installed in the correct environment.
- **Static Fallback**: This project was self-generated due to API restrictions on primary discovery sources (e.g., Reddit).

## Note
This repository was published under `fairyfemirins/sessionscribe-1780103169` due to namespace restrictions.
To transfer to `femirins/sessionscribe`:
1. Go to: [https://github.com/fairyfemirins/sessionscribe-1780103169/settings](https://github.com/fairyfemirins/sessionscribe-1780103169/settings)
2. Under "Danger Zone", select "Transfer repository".
3. Enter `femirins/sessionscribe` as the new owner.

## License
MIT