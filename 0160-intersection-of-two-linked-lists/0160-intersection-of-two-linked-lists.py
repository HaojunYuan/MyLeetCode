# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l1 = 0
        l2 = 0
        curr1 = headA
        while curr1:
            l1 += 1
            curr1 = curr1.next
            
        curr2 = headB
        while curr2:
            l2 += 1
            curr2 = curr2.next
        
        curr1, curr2 = headA, headB
        if l1 < l2:
            l1, l2 = l2, l1
            curr1, curr2 = headB, headA
        
        for _ in range(l1 - l2):
            curr1 = curr1.next
        
        while curr1 and curr2:
            if curr1 == curr2:
                return curr1
            curr1 = curr1.next
            curr2 = curr2.next
        return None