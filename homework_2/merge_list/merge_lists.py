class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def is_sorted(head: ListNode) -> bool:
    while head and head.next:
        if head.val > head.next.val:
            return False
        head = head.next
    return True

def list_to_linked(lst):
    dummy = ListNode()
    tail = dummy
    for val in lst:
        tail.next = ListNode(val)
        tail = tail.next
    return dummy.next

def linked_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

def merge_with_dummy(list1: ListNode, list2: ListNode) -> ListNode:
    if not is_sorted(list1) or not is_sorted(list2):
        raise ValueError("1 или оба листа не являются отсортированным списком")
    
    if not list1:
        return list2
    if not list2:
        return list1

    dummy = ListNode()
    tail = dummy

    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    tail.next = list1 if list1 else list2

    return dummy.next

def merge_without_dummy(list1: ListNode, list2: ListNode) -> ListNode:
    if not is_sorted(list1) or not is_sorted(list2):
        raise ValueError("1 или оба листа не являются отсортированным списком")

    if not list1:
        return list2
    if not list2:
        return list1

    if list1.val < list2.val:
        head = list1
        list1 = list1.next
    else:
        head = list2
        list2 = list2.next

    current = head

    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    current.next = list1 if list1 else list2
    return head


if __name__ == "__main__":
    arr1 = list(map(int, input("1 Массив: ").split()))
    arr2 = list(map(int, input("2 Массив: ").split()))

    l1 = list_to_linked(arr1)
    l2 = list_to_linked(arr2)

    merged_dummy = merge_with_dummy(l1, l2)
    print("Результат слияния с фиктивгым элементом: ", linked_to_list(merged_dummy))

    l1 = list_to_linked(arr1)
    l2 = list_to_linked(arr2)
    merged_no_dummy = merge_without_dummy(l1, l2)
    print("Результат слияние без фиктивного элемента", linked_to_list(merged_no_dummy))