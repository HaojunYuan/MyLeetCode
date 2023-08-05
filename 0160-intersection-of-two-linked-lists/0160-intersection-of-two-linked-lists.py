# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA=self.getLen(headA)
        lenB=self.getLen(headB)
        curr1=headA
        curr2=headB
        while lenA>lenB:
            curr1=curr1.next
            lenA-=1
        while lenB>lenA:
            curr2=curr2.next
            lenB-=1
        
        while curr1 and curr2:
            if curr1==curr2:
                return curr1
            curr1=curr1.next
            curr2=curr2.next
        return None
            
    
    def getLen(self, head):
        n=0
        while head:
            n+=1
            head=head.next
        return n