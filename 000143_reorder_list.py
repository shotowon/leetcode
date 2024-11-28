from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList__withAdditionalList(
        self, head: Optional[ListNode]
    ) -> None:
        elements = []
        el = head
        while el is not None:
            elements.append(el)
            el = el.next
        l, r = 0, len(elements) - 1
        while l < r - 1:
            elements[l].next = elements[r]
            l += 1
            elements[r].next = elements[l]
            r -= 1
        elements[r].next = None

    # without that list
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr = slow.next
        prev = slow.next = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        first, second = head, prev
        while second:
            fnext, snext = first.next, second.next
            first.next = second
            second.next = fnext
            first = fnext
            second = snext
