# SessionScribe: Reproducible Tutorial

## Prerequisites
- Python 3.11+
- `pip` (Python package manager)

## Installation
```bash
# Clone the repository
git clone https://github.com/femirins/sessionscribe.git
cd sessionscribe

# Create a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Usage
### 1. Start Recording
```bash
# Start a new session
sessionscribe start

# Run commands (e.g., ls, echo, git)
echo "Hello, World!"
ls -la

# Stop recording (Ctrl+D or type 'exit')
exit
```

### 2. Generate Markdown
```bash
# Stop recording and generate SESSION.md
sessionscribe stop
```

### 3. Exclude Sensitive Data
```bash
# Start recording with --exclude-sensitive
sessionscribe start --exclude-sensitive
```

## Output
A `SESSION.md` file is generated in the current directory:

```markdown
# Terminal Session: 2026-05-29 20:00:00

**Command:** `echo "Hello, World!"`

**Output:**
```
Hello, World!
```

**Command:** `ls -la`

**Output:**
```
-rw-r--r--  1 user  staff   123 May 29 19:59 README.md
```
```