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
        copy=defaultdict(lambda:Node(0))
        copy[None]=None
        temp=head
        while temp:
            copy[temp].val=temp.val
            copy[temp].next=copy[temp.next]
            copy[temp].random=copy[temp.random]
            temp=temp.next
        return copy[head]