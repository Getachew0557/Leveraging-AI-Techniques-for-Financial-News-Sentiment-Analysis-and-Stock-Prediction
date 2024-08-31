# tests/test.py

import pytest

# Example function to test
def add(a, b):
    return a + b

# Example test case
def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

# You can add more tests here for other parts of your code
