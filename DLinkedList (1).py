# class Node:
#     def __init__(self,value):
#         self.next=None
#         self.prev=None
#         self.value=value
# class DLinkedList:
#     def __init__(self):
#         self.head=None
#         self.tail=None
#         self.size=0
#     def __iter__(self):
#         tempNode = self.head
#         while tempNode:
#             yield tempNode
#             tempNode=tempNode.next
#     def create(self,value):
#         newNode=Node(value)
#         self.head=newNode
#         self.tail=newNode
#         # newNode.next=None
#         # newNode.prev=None
#         self.size +=1
#     def traverse(self):
#         tempNode = self.head
#         while tempNode:
#             print(tempNode.value,end=" --> ")
#             tempNode=tempNode.next
#         print()
#     def reverseTraverse(self):
#         tempNode=self.tail
#         while tempNode:
#             print(tempNode.value,end=" --> ")
#             tempNode=tempNode.prev
#         print()
#     def insert(self,value,location):
#         if self.head is None:
#             self.create(value)
#         else:
#             newNode = Node(value)
#             if location == 0:
#                 newNode.next=self.head
#                 newNode.prev=None
#                 self.head.prev=newNode
#                 self.head = newNode
#                 self.size+=1
#             elif location >= self.size:
#                 self.tail.next=newNode
#                 newNode.next=None
#                 newNode.prev=self.tail
#                 self.tail = newNode
#             else:
#                 tempNode=self.head
#                 index=0
#                 while index<location-1:
#                     tempNode=tempNode.next
#                     index+=1
#                 newNode.next = tempNode.next
#                 newNode.prev = tempNode
#                 tempNode.next=newNode
#                 newNode.next.prev = newNode
#                 self.size +=1
#         print("successfully inserted node")

class Node:
    def __init__(self,value):
        self.next=None
        self.prev=None
        self.value=value

class DLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0

    def __iter__(self):
        tempNode = self.head
        while tempNode:
            yield tempNode
            tempNode=tempNode.next
    def create(self,value):
        newNode=Node(value)
        self.head=newNode
        self.tail=newNode
        # newNode.next=None
        # newNode.prev=None
        self.size +=1
    def traverse(self):
        tempNode = self.head
        while tempNode:
            print(tempNode.value,end=" --> ")
            tempNode=tempNode.next
        print()
    def reverseTraverse(self):
        tempNode=self.tail
        while tempNode:
            print(tempNode.value,end=" --> ")
            tempNode=tempNode.prev
        print()
    def insert(self,value,location):
        if self.head is None:
            self.create(value)
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next=self.head
                newNode.prev=None
                self.head.prev=newNode
                self.head = newNode
                self.size+=1
            elif location >= self.size:
                self.tail.next=newNode
                newNode.next=None
                newNode.prev=self.tail
                self.tail = newNode
                self.size+=1
            else:
                tempNode=self.head
                index=0
                while index<location-1:
                    tempNode=tempNode.next
                    index+=1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                tempNode.next=newNode
                newNode.next.prev = newNode
                self.size+=1
        print("successfully inserted node")



dll = DLinkedList()
dll.create(0)
dll.insert(1,1)
dll.insert(2,2)
dll.insert(5,20)
dll.traverse()
dll.reverseTraverse()


# dll = DLinkedList()
# dll.create(0)
# dll.insert(1,1)
# dll.insert(2,2)
# dll.traverse()
# dll.reverseTraverse()
