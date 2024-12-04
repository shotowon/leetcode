from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self,
                      l1: Optional[ListNode],
                      l2: Optional[ListNode]
                      ) -> Optional[ListNode]:
        result_prev = ListNode()
        curr = result_prev

        carry = False
        while l1 or l2 or carry:
            v1, v2 = l1.val if l1 else 0, l2.val if l2 else 0
            val = v1 + v2 + (1 if carry else 0)
            carry = val >= 10
            val = val - (10 if carry else 0)
            curr.next = ListNode(val)

            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return result_prev.next
