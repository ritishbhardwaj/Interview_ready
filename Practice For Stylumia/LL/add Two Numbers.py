

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
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2:
            return None
        s1 = 0
        s2 = 0
        i=-1    
        while l1:
            i+=1
            s1+=(10**(i))*l1.val
            l1= l1.next
        i=-1    
        while l2:
            i+=1
            s2+=(10**(i))*l2.val
            l2= l2.next
        number = str(s1+s2)
        node = ListNode(0)
        ans = node
        for i in range(len(number)-1,-1,-1):
            ans.next = ListNode(int(number[i]))
            ans=ans.next
        return node.next
    

head=ListNode(2)
head.next=ListNode(4)
head.next.next=ListNode(3)
# head.next.next.next=ListNode(4)
# head.next.next.next.next=ListNode(5)
# head.next.next.next.next.next=ListNode(6)
head1=ListNode(5)
head1.next=ListNode(6)
head1.next.next=ListNode(4)

obj=Solution()
pointer=obj.addTwoNumbers(head,head1)
printt(pointer)