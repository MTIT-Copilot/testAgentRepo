import pytest

from agentlab.cli import main


def test_main_greets_name(capsys):
    """Test that main() prints greeting for provided name."""
    result = main(["Tayyab"])
    captured = capsys.readouterr()
    assert captured.out == "Hello, Tayyab!\n"
    assert result == 0


def test_main_help_option(capsys):
    """Test that --help option displays help message."""
    with pytest.raises(SystemExit) as excinfo:
        main(["--help"])
    assert excinfo.value.code == 0
    captured = capsys.readouterr()
    assert "Agent Lab CLI" in captured.out
    assert "Name to greet" in captured.out
