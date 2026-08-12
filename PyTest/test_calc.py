import pytest
import calc

def test_add():
    assert calc.add(3, 4) == 7

def test_add_negative():
    assert calc.add(-3, 4) == 1

def test_invalid():
    with pytest.raises(ValueError):
        calc.div(9, 0)