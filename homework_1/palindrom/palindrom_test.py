from palindrom import is_palindrom

def test_basefunc():
    assert is_palindrom('525') is True
    assert is_palindrom("121") is True
    assert is_palindrom("31") is False
    assert is_palindrom("1232") is False

def test_text():
    assert is_palindrom('qwerty') is False

def test_float():
    assert is_palindrom('1.1') is False
    assert is_palindrom('1,1') is False

def test_strip():
    assert is_palindrom(' 525 \t') is True
    assert is_palindrom(" 121") is True
    assert is_palindrom("\n 313") is True
    assert is_palindrom("12321\xa0 ") is True

