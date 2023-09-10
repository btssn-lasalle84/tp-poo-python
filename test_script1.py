import pytest;
import runpy;
from io import StringIO

def test_script1(monkeypatch,capfd):
    # simule une saisie
    monkeypatch.setattr('sys.stdin', StringIO('3\n'))
    # simule input()
    #monkeypatch.setattr('builtins.input', lambda _: "3")
    runpy.run_path("script1.py")
    out, err = capfd.readouterr()
    assert out == "9\n"
