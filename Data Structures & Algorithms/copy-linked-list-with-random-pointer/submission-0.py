"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mapping = {None : None}

        current = head
        while current:
            mapping[current] = Node(current.val)
            current = current.next
        
        current = head
        while current:
            copy = mapping[current]
            copy.random = mapping[current.random]
            copy.next = mapping[current.next]
            current = current.next

        return mapping[head]
        