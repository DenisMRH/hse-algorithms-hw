import pytest
from anagrams import group_anagrams


def test_example_from_prompt_exact_order():
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    expected = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    assert group_anagrams(strs) == expected


def test_empty_input():
    assert group_anagrams([]) == []


def test_singletons():
    strs = ["c", "b", "a"]
    expected = [["a"], ["b"], ["c"]]
    assert group_anagrams(strs) == expected


def test_case_sensitivity():
    strs = ["eat", "Tea", "tae"]
    expected = [["Tea"], ["eat", "tae"]]
    assert group_anagrams(strs) == expected


def test_with_empty_strings():
    strs = ["", "", "a"]
    expected = [["a"], ["", ""]]
    assert group_anagrams(strs) == expected


def test_duplicates_inside_group():
    strs = ["ab", "ba", "ab"]
    expected = [["ab", "ab", "ba"]]
    assert group_anagrams(strs) == expected


def test_numbers_and_mixed():
    strs = ["123", "231", "312", "12", "21", "a1", "1a"]
    expected = [["12", "21"], ["1a", "a1"], ["123", "231", "312"]]
    assert group_anagrams(strs) == expected


def test_order_independence_of_input():
    a = ["eat", "tea", "tan", "ate", "nat", "bat"]
    b = list(reversed(a))
    assert group_anagrams(a) == group_anagrams(b)


def test_flatten_equals_input_multiset():
    strs = ["ab", "ba", "ab", "xyz", "yxz", "zxy", "solo"]
    grouped = group_anagrams(strs)
    flattened = [w for g in grouped for w in g]
    assert sorted(flattened) == sorted(strs)
