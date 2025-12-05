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

def test_cli_greeting_different_name(capsys):
    rc = main(["Alice"])
    out, err = capsys.readouterr()
    assert rc == 0
    assert "Hello, Alice!" in out

def test_cli_help_shows_description(capsys):
    with pytest.raises(SystemExit):
        main(["--help"])
    out, err = capsys.readouterr()
    assert "Agent Lab CLI" in out
