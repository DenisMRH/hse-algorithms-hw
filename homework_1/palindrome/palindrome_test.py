from palindrome import is_palindrome

def test_basefunc():
    assert is_palindrome('525') is True
    assert is_palindrome("121") is True
    assert is_palindrome("31") is False
    assert is_palindrome("1232") is False

def test_text():
    assert is_palindrome('qwerty') is False

def test_float():
    assert is_palindrome('1.1') is False
    assert is_palindrome('1,1') is False

def test_strip():
    assert is_palindrome(' 525 \t') is True
    assert is_palindrome(" 121") is True
    assert is_palindrome("\n 313") is True
    assert is_palindrome("12321\xa0 ") is True

