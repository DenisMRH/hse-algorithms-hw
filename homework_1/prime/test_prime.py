import pytest
from prime import count_prime

def test_basefunc():
    assert count_prime("10") == 4
    assert count_prime("1") == 0

def test_space():
    assert count_prime("\t10") == 4
    assert count_prime("  12  ") == 5
    assert count_prime("\xa01") == 0
    assert count_prime("\n15") == 6

def test_value_error():
    with pytest.raises(ValueError):
        count_prime("text")
    with pytest.raises(ValueError):
        count_prime("")
