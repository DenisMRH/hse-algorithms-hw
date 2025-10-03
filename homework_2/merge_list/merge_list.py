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

def merge_with_dummy(list1: ListNode, list2: ListNode) -> ListNode:
    if not is_sorted(list1) or not is_sorted(list2):
        raise ValueError("1 или оба листа не являются отсортированным списком")
    
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