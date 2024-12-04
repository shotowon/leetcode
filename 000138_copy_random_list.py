from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        ptr = head
        nodes = {None: None}

        while ptr:
            copy = Node(ptr.val)
            nodes[ptr] = copy
            ptr = ptr.next

        ptr = head
        while ptr:
            copy = nodes[ptr]
            copy.next = nodes[ptr.next]
            copy.random = nodes[ptr.random]
            ptr = ptr.next

        return nodes[head]
