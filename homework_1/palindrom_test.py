from palindrom import is_palindrom

def test_examples():
    assert is_palindrom(121) is True
    assert is_palindrom(31) is False

def test_more():
    assert is_palindrom(1) is True
    assert is_palindrom(1221) is True
    assert is_palindrom(12345) is False
    assert is_palindrom(-121) is False
