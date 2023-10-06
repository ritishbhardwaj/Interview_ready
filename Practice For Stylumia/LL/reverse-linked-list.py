from typing import *
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def printt(head:Optional[ListNode]):
    t=head
    while t:
        print(t.val,end=" ")
        t=t.next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next==None:
            return head
        t,v=head,head.next
        ref=None
        while v != None:
            t.next=ref
            ref=t
            t=v
            v=v.next
        t.next=ref

        return t





head=ListNode()
# head.next=ListNode(2)
# head.next.next=ListNode(3)
# head.next.next.next=ListNode(4)
# head.next.next.next.next=ListNode(5)
# head.next.next.next.next.next=ListNode(6)


obj=Solution()
pointer=obj.reverseList(head)
printt(pointer)