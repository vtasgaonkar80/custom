"""this is a pytest file"""

from app import custom


def test_fun():
    """docstring"""
    assert custom() == "Hello"
