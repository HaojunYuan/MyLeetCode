# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=pretail=ListNode()
        dummy.next=l=r=head
        
        while True:
            count=0
            while r and count<k:
                count+=1
                r=r.next
            #r is now at the head of the next k group
            if count==k:
                pre,cur=r,l
                #reverse linked list for current k group
                for _ in range(k):
                    temp=cur.next
                    cur.next=pre
                    pre=cur
                    cur=temp
                #connect the previous tail to the head of current k group
                pretail.next=pre
                #move the previous tail to the tail of current k group
                pretail=l
                #move l and r pointers to the head of next k group
                l=r
            else:
                return dummy.next
                