# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # merge sort
        return self.process(head)
    
    def process(self, node):
        if not node:
            return
        if not node.next:
            return node
        dummy = ListNode(0, node)
        mid = self.findMid(dummy)
        left = dummy.next
        right = mid.next
        mid.next = None
        sortedLeft = self.process(left)
        sortedRight = self.process(right)
        return self.merge(sortedLeft, sortedRight)
    
    def merge(self, l, r):
        dummy = curr = ListNode()
        while l and r:
            if l.val < r.val:
                curr.next = l
                l = l.next
            else:
                curr.next = r
                r = r.next
            curr = curr.next
        
        curr.next = l or r
        return dummy.next
        
    
    def findMid(self, node):
        slow = fast = node
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow