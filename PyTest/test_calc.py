import pytest
import calc

# def test_add():
#     assert calc.add(3, 4) == 7

# def test_add_negative():
#     assert calc.add(-3, 4) == 1
#     assert calc.add(-3, 4) == 3

# def test_invalid():
#     with pytest.raises(ValueError):
#         calc.div(9, 0)

# def test_mult():
#     assert calc.mult(4, 5) == 20

@pytest.fixture
def user():
    return {"name": "Alice", "age":25}

def test_user(user):
    assert user["name"] == "Alice"

@pytest.mark.slow
def test_something():
    print("Hello")
    assert 5 == 5

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (10, 20, 30),
    (0, 5, 5),
])
def test_add(a, b, expected):
    assert a + b == expected
