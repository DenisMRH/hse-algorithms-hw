import pytest
from sum import max_even_sum

def test_basefunc():
    assert max_even_sum("5 7 13 2 14") == 36  
    assert max_even_sum("78 2 12 4 1 3 1") == 100  

def test_onedigit():
    assert max_even_sum("3") == 0  
    assert max_even_sum("5") == 0  
    assert max_even_sum("4") == 4  

def test_space():
    assert max_even_sum(" 1       3     5 ") == 8 
    assert max_even_sum("1\t3 5") == 8 
    assert max_even_sum("1\xa03 5") == 8 
    assert max_even_sum("1\n3 5") == 8 

def test_valueerror():
    with pytest.raises(ValueError):
        max_even_sum("1 text 5")

def test_all_odd():
    assert max_even_sum("1 3 5") == 8 

def test_one_even_one_odd():
    assert max_even_sum("2 3") == 2 

def test_empty():
    assert max_even_sum("") == 0 
    assert max_even_sum(" ") == 0 
    assert max_even_sum("\t") == 0 
