# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        
        fast=slow=curr=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        stack=[]
        while slow:
            stack.append(slow.val)
            slow=slow.next
        
        while stack:
            if stack.pop()!=curr.val:
                return False
            curr=curr.next
        return True