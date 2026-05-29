import os
import tempfile
from click.testing import CliRunner
from sessionscribe import cli

def test_start_stop():
    """Test start and stop commands."""
    runner = CliRunner()
    
    # Start recording
    result = runner.invoke(cli, ["start"], input="echo 'Hello, World!'\nexit\n")
    assert result.exit_code == 0
    assert "Recording started" in result.output
    
    # Stop recording
    result = runner.invoke(cli, ["stop"])
    assert result.exit_code == 0
    assert "Session saved to SESSION.md" in result.output
    assert os.path.exists("SESSION.md")
    
    # Cleanup
    os.remove("SESSION.md")

def test_exclude_sensitive():
    """Test --exclude-sensitive flag."""
    runner = CliRunner()
    
    # Start recording with --exclude-sensitive
    result = runner.invoke(cli, ["start", "--exclude-sensitive"], input="echo 'My password is 12345'\nexit\n")
    assert result.exit_code == 0
    
    # Stop recording
    result = runner.invoke(cli, ["stop"])
    assert result.exit_code == 0
    
    # Check if sensitive data was redacted
    with open("SESSION.md", "r") as f:
        content = f.read()
        assert "[REDACTED]" in content
    
    # Cleanup
    os.remove("SESSION.md")