# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def findIntersect(self,head):
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return slow

        return None
    
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        intersect=self.findIntersect(head)
        if not intersect:
            return None
        pt1=head
        pt2=intersect
        while pt1!=pt2:
            pt1=pt1.next
            pt2=pt2.next
        return pt1