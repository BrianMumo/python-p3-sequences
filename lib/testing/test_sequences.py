import pytest
from sequences import print_fibonacci

def test_fibonacci_length_zero():
    assert print_fibonacci(0) == []

def test_fibonacci_length_one():
    assert print_fibonacci(1) == [0]

def test_fibonacci_length_two():
    assert print_fibonacci(2) == [0, 1]

def test_fibonacci_length_nine():
    assert print_fibonacci(9) == [0, 1, 1, 2, 3, 5, 8, 13, 21]
