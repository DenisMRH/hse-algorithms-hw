from palindrom import is_palindrom

def test_strip():
    assert is_palindrom(' 525 \t') is True
    assert is_palindrom(" 121") is True
    assert is_palindrom("\n 313") is True
    assert is_palindrom("12321\xa0 ") is True

