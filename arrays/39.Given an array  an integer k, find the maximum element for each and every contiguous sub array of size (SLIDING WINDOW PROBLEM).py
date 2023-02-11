# Implementation using DLL

# class node:
#     def __init__(self,key):
#         self.key=key
#         self.next=None
#         self.previous=None
#
# def print_ji(head):
#     t=head
#     while t:
#         print(t.key)
#         t=t.next
#     return
#
# def Sliding_Window_Max(arr,head):
#     pass
#
# head=node(0)
# temp1=node(1)
# temp2=node(2)
# temp3=node(3)
#
# head.next=temp1
# temp1.previous=head
# temp1.next=temp2
# temp2.previous=temp1
# temp2.next=temp3
# temp3.previous=temp2
#
# print_ji(head)
#
# arr=[10,4,2,11,3,15,12,8,7,9,21,14]
# Sliding_Window_Max(arr,head)

#  Implementation using Deque

from collections import deque,defaultdict

def Sliding_Window_Max(arr,k):
    dq=deque()
    ans=[]
    if not arr:
        return False
    if len(arr)*k==0:
        return []

    for i in range(len(arr)):
        if dq and dq[0]==i-k:
            dq.popleft()
        dq.append(i)
    # print(dq)
        while dq and arr[i]>=arr[dq[-1]]:
            dq.pop()
        # print(dq)

arr=[10,4,22,11,3,15,12,8,7,9,21,14]
window=3
Sliding_Window_Max(arr,window)