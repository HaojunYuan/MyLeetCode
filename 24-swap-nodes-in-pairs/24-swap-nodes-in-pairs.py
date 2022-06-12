# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=pre=ListNode(0,head)
        while pre.next and pre.next.next:
            #Getting the two nodes
            a=pre.next
            b=pre.next.next
            #Swapping
            pre.next=b
            a.next=b.next
            b.next=a
            #Move the pre pointer to a
            pre=a
        return dummy.next