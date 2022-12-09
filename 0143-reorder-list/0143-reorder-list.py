# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        pre=None
        curr=slow
        while curr:
            temp=curr.next
            curr.next=pre
            pre=curr
            curr=temp
        
        l1,l2=head,pre
        while l2.next:
            l1.next,l1=l2,l1.next
            l2.next,l2=l1,l2.next