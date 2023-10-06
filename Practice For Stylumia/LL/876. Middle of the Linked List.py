from typing import *
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def printt(head:Optional[ListNode]):
    t=head
    print(t.val)
    # while t:
    #     print(t.val,end=" ")
    #     t=t.next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return head
        
        cnt=head
        middle=head
        count=0

        while cnt !=None:
            count+=1
            cnt=cnt.next
        print(count)

        count=count//2

        for i in range(count):
            middle=middle.next
        
        return middle



head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(3)
head.next.next.next=ListNode(4)
head.next.next.next.next=ListNode(5)
# head.next.next.next.next.next=ListNode(6)


obj=Solution()
pointer=obj.middleNode(head)
printt(pointer)