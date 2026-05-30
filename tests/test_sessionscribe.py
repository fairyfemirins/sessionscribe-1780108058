import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sessionscribe import TerminalRecorder

def test_recorder():
    recorder = TerminalRecorder(exclude_sensitive=False)
    test_data = b"echo 'Hello, World!'\\nHello, World!\\n$ "
    recorder.feed(test_data)
    md_content = recorder.generate_markdown()
    assert "echo 'Hello, World!'" in md_content
    assert "Hello, World!" in md_content
    assert "Timestamp" in md_content

def test_sensitive_data_exclusion():
    recorder = TerminalRecorder(exclude_sensitive=True)
    test_data = b"echo 'My password is 12345'\\nMy password is 12345\\n$ "
    recorder.feed(test_data)
    md_content = recorder.generate_markdown()
    assert "[REDACTED]" in md_content