import pytest

from agentlab.cli import main


def test_cli_help_shows_usage(capsys):
    # argparse prints help and exits with SystemExit
    with pytest.raises(SystemExit):
        main(["--help"])
    out, err = capsys.readouterr()
    assert "usage:" in out.lower()

def test_cli_greeting_prints_name(capsys):
    rc = main(["Tayyab"])
    out, err = capsys.readouterr()
    assert rc == 0
    assert "Hello, Tayyab!" in out


def test_cli_greeting_alice(capsys):
    rc = main(["Alice"])
    out, err = capsys.readouterr()
    assert rc == 0
    assert "Hello, Alice!" in out


def test_cli_greeting_bob(capsys):
    rc = main(["Bob"])
    out, err = capsys.readouterr()
    assert rc == 0
    assert "Hello, Bob!" in out


def test_cli_greeting_with_spaces(capsys):
    rc = main(["John Doe"])
    out, err = capsys.readouterr()
    assert rc == 0
    assert "Hello, John Doe!" in out


def test_cli_greeting_special_chars(capsys):
    rc = main(["O'Brien"])
    out, err = capsys.readouterr()
    assert rc == 0
    assert "Hello, O'Brien!" in out


def test_cli_greeting_long_name(capsys):
    rc = main(["VeryLongNameWithManyCharacters"])
    out, err = capsys.readouterr()
    assert rc == 0
    assert "Hello, VeryLongNameWithManyCharacters!" in out


def test_cli_greeting_numeric_name(capsys):
    rc = main(["123"])
    out, err = capsys.readouterr()
    assert rc == 0
    assert "Hello, 123!" in out


def test_cli_missing_argument():
    # Missing required name argument should exit with error
    with pytest.raises(SystemExit) as exc_info:
        main([])
    assert exc_info.value.code != 0
