# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = prev = ListNode(0, head)
        curr = head
        while curr and curr.next:
            prev.next = curr.next
            newStart = curr.next.next
            curr.next.next = curr
            curr.next = newStart
            prev = curr
            curr = curr.next
        return dummy.next
        
            