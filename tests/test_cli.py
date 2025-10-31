import pytest

from agentlab.cli import build_parser, main


def test_cli_greeting_path(capsys):
    """Test that CLI greets the provided name."""
    result = main(["Alice"])
    captured = capsys.readouterr()
    assert result == 0
    assert captured.out == "Hello, Alice!\n"


def test_cli_greeting_different_name(capsys):
    """Test CLI with a different name."""
    result = main(["Bob"])
    captured = capsys.readouterr()
    assert result == 0
    assert captured.out == "Hello, Bob!\n"


def test_cli_help():
    """Test that --help flag works without errors."""
    parser = build_parser()
    with pytest.raises(SystemExit) as exc_info:
        parser.parse_args(["--help"])
    assert exc_info.value.code == 0


def test_build_parser_structure():
    """Test that parser is configured correctly."""
    parser = build_parser()
    assert parser.prog == "agentlab"
    assert parser.description == "Agent Lab CLI"
