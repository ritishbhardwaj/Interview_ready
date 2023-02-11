class Node:
    def __init__(self,value):
        self.next =None
        self.value=value
        self.back =None

class DLinkedList:
    def __int__(self):
        self.head =None
        self.tail=None
    def __iter__(self):
        node =self.head
        while node:
            yield node
            node = node.next
    def create(self,value):  # ------------------------>O(1)
        node =Node(value)  # ------------------------>O(1)
        node.next =None  # ------------------------>O(1)
        node.back = None  # ------------------------>O(1)
        self.head = node  # ------------------------>O(1)
        self.tail = node  # ------------------------>O(1)
        print("Successfully created linked list")  # ------------------------>O(1)
    def insert(self,value,location):
        if self.head is None:
            print('Node cannot be inserted')
        else:
            newNode = Node(value)
            if location == 0:
                newNode.back=None
                newNode.next=self.head
                self.head.back=newNode
                self.head=newNode
            if location == -1:
                newNode.next=None
                newNode.back=self.tail
                self.tail.next =newNode
                self.tail=newNode
            else:
                temp = self.head
                index=0
                while index<location -1:
                    temp =temp.next
                    index+=1
                newNode.next = temp.next
                newNode.back=temp
                temp.next = newNode
                newNode.next.back=newNode
    def traverse(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp = self.head
            while temp:
                print(temp.value,end=" --> ")
                temp=temp.next
            print()
    def reverseTraverse(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp = self.tail
            # print(temp.value)
            while temp:
                print(temp.value,end=" --> ")
                temp=temp.back
            print()
    def search(self,value):
        location = 0
        temp =self.head
        while temp:
            if(temp.value==value):
                return (f"found {value} at location {location}")
            temp=temp.next
            location+=1
        return (f"value not found")
    def delete(self,location):
        if self.head is None:
            print("No element present to be deleted")
        else:
            if location == 0:
                if self.head == self.tail==None:
                    self.head = None
                    self.tail=None
                else:
                    self.head = self.head.next
                    self.head.back=None
            elif location ==1:
                if self.head == self.tail==None:
                    self.head = None
                    self.tail=None
                else:
                    self.tail=self.tail.back
                    self.tail.next=None
            else:
                temp = self.head
                index =0
                while index < location -1:
                    temp=temp.next
                    index+=1
                temp.next=temp.next.next
                temp.next.back=temp
        print("The node has beeen Successfully deleted")

    def deleteEntire(self):
        if self.head is None:
            print("Linked list doesnot exist")
        else:
            temp=self.head
            while temp:
                temp.back =None
                temp=temp.next
            self.head=None
            self.tail=None
            print("Linkes list deleted Successfully")



dll = DLinkedList()
dll.create(5)
dll.insert(13,0)
dll.insert(33,0)
print([node.value for node in dll])
dll.traverse()
dll.reverseTraverse()
dll.delete(2)
dll.traverse()
# print(dll.search(13))
# dll.deleteEntire()
