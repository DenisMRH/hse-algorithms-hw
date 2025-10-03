import pytest
from merge_lists import (
    ListNode,
    list_to_linked,
    linked_to_list,
    merge_with_dummy,
    merge_without_dummy,
)

def test_merge_with_dummy_basic():
    l1 = list_to_linked([1, 2, 4])
    l2 = list_to_linked([1, 3, 4])
    merged = merge_with_dummy(l1, l2)
    assert linked_to_list(merged) == [1, 1, 2, 3, 4, 4]

def test_merge_without_dummy_basic():
    l1 = list_to_linked([1, 2, 4])
    l2 = list_to_linked([1, 3, 4])
    merged = merge_without_dummy(l1, l2)
    assert linked_to_list(merged) == [1, 1, 2, 3, 4, 4]

def test_merge_with_dummy_one_empty():
    l1 = list_to_linked([])
    l2 = list_to_linked([1, 2, 3])
    merged = merge_with_dummy(l1, l2)
    assert linked_to_list(merged) == [1, 2, 3]

def test_merge_without_dummy_one_empty():
    l1 = list_to_linked([1, 2, 3])
    l2 = list_to_linked([])
    merged = merge_without_dummy(l1, l2)
    assert linked_to_list(merged) == [1, 2, 3]

def test_merge_both_empty():
    l1 = list_to_linked([])
    l2 = list_to_linked([])
    merged = merge_with_dummy(l1, l2)
    assert linked_to_list(merged) == []

def test_merge_raises_on_unsorted():
    l1 = list_to_linked([1, 5, 3]) 
    l2 = list_to_linked([1, 2, 3])
    with pytest.raises(ValueError):
        merge_with_dummy(l1, l2)

    l1 = list_to_linked([1, 5, 3])
    l2 = list_to_linked([1, 2, 3])
    with pytest.raises(ValueError):
        merge_without_dummy(l1, l2)
