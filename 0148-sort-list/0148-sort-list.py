# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # merge sort, split from middle and merge
        # find middle node
        return self.process(head)
    
    def process(self, node):
        if not node:
            return
        if not node.next:
            return node
        firstHalf, secondHalf = self.splitMid(node)
        sortedFirstHalf = self.process(firstHalf)
        sortedSecondHalf = self.process(secondHalf)
        return self.merge(sortedFirstHalf, sortedSecondHalf)
    
    def merge(self, a, b):
        # merge two sorted linked list
        dummy = curr = ListNode()
        while a and b:
            if a.val < b.val:
                curr.next = a
                a = a.next
            else:
                curr.next = b
                b = b.next
            curr = curr.next
        curr.next = a or b
        return dummy.next
    
    def splitMid(self, head):
        dummy = ListNode(0, head)
        slow = fast = dummy
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        secondhalf = slow.next
        slow.next = None
        return head, secondhalf