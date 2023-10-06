from typing import *
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def printt(head:Optional[ListNode]):
    t=head
    # print(t.val)
    while t:
        print(t.val,end=" ")
        t=t.next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        startNode=ListNode()
        startNode.next=head
        fast=startNode
        slow=startNode

        for i in range(1,n+1):
            fast=fast.next

        while fast.next!=None:
            fast=fast.next
            slow=slow.next
        
        slow.next=slow.next.next

        return startNode.next

    





head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(3)
head.next.next.next=ListNode(4)
head.next.next.next.next=ListNode(5)
head.next.next.next.next.next=ListNode(6)

obj=Solution()
pouinter=obj.removeNthFromEnd(head,n=6)

printt(pouinter)