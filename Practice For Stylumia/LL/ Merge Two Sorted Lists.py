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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1==None or list2==None:
            return list1 if list2==None else list2
        
        l1,l2=list1,list2
        if l1.val>l2.val:
            t=l2
            l2=l1
            l1=t
            
        res=l1
        while l1!=None and l2!=None:
            temp=None
            while l1!=None and l1.val<=l2.val:
                temp=l1
                l1=l1.next
            temp.next=l2

            tmp=l1
            l1=l2
            l2=tmp
        
        return res



head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(4)
# head.next.next.next=ListNode(4)
# head.next.next.next.next=ListNode(5)
# head.next.next.next.next.next=ListNode(6)
head1=ListNode(1)
head1.next=ListNode(3)
head1.next.next=ListNode(4)


obj=Solution()
pointer=obj.mergeTwoLists(head,head1)

printt(pointer)