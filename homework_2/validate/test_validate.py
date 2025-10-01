import pytest
from validate import validate_stack_sequences

def test_basic_examples():
    assert validate_stack_sequences([1,2,3,4,5], [1,3,5,4,2]) is True
    assert validate_stack_sequences([1,2,3], [3,1,2]) is False

def test_simple_and_edge_cases():
    assert validate_stack_sequences([1], [1]) is True
    assert validate_stack_sequences([1,2], [2,1]) is True
    assert validate_stack_sequences([1,2,3], [1,2,3]) is True
    assert validate_stack_sequences([1,2,3], [3,2,1]) is True
    assert validate_stack_sequences([1,2,3], [1,3,2]) is True
    assert validate_stack_sequences([1,2,3], [2,3,1]) is True
    assert validate_stack_sequences([1,2,3,4], [2,4,3,1]) is True
    assert validate_stack_sequences([1,2,3,4], [3,1,4,2]) is False

def test_invalid_lengths_and_permutations():
    assert validate_stack_sequences([1], []) is False
    assert validate_stack_sequences([1,2], [1,2,3]) is False
    assert validate_stack_sequences([1,2,3], [1,2,4]) is False
    assert validate_stack_sequences([1,2,3], [1,2,2]) is False

def test_arbitrary_values():
    assert validate_stack_sequences([10,20,30,40], [20,10,40,30]) is True
    assert validate_stack_sequences([-1,-2,-3], [-2,-3,-1]) is True
    assert validate_stack_sequences([100,3,50], [50,3,100]) is True
    assert validate_stack_sequences([100,3,50], [3,100,50]) is True

def test_empty_lists():
    assert validate_stack_sequences([], []) is False
