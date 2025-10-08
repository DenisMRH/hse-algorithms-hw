import pytest
from two_sum import two_sum

def test_from_example():
    assert two_sum(["1", "3", "4", "10"],"7") == (1, 2)
    assert two_sum(["5", "5", "1", "4"],"10") == (0, 1)

def test_negative_numbers():
    assert two_sum(["-1","5","6","1"],"0") == (0, 3)
    assert two_sum(["1", "-6", "-7", "0"],"-6") == (0, 2)

def test_not_a_digit():
    with pytest.raises(ValueError):
        assert two_sum(["abc","5","6","1"],"0")
    with pytest.raises(ValueError):
        assert two_sum(["1", "-6", "-7", "0"],"abc") 

def test_wrong_input():
    with pytest.raises(ValueError):
        assert two_sum(["1","2","3","4"],"")
    with pytest.raises(ValueError):
        assert two_sum(["1"],"1")