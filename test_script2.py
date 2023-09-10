import script2;
import pytest;

def test_script2():
    F = script2.convertirCelsiusVersFahrenheit(22)
    assert F == pytest.approx(71.6, 0.1)
    F = script2.convertirCelsiusVersFahrenheit(0)
    assert F == 32
    F = script2.convertirCelsiusVersFahrenheit(-100)
    assert F == -148
