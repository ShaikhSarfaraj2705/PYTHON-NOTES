class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None

    def insert(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=new_node

    def display(self):
        if self.head is None:
            print("linked list is empty")
            return
        temp=self.head
        while temp:
            print(temp.data,end="->")
            temp=temp.next
        print("None")

    def delete(self,key):
        temp=self.head
        if temp and temp.data==key:
            self.head=temp.next
            temp=None 
            return
        prev =None
        while temp and temp.data!=key:
            prev=temp
            temp=temp.next
        if temp is None:
            print(f"{key} not found in list")
            return
        prev.next=temp.next
        temp=None

ll=LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.display()
ll.delete(20)
ll.display()