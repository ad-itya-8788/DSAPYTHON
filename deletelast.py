class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
class Linkedlist:
  def __init__(self):
    self.head=None
  def create(self,data):
    newnode=Node(data)
    if self.head is None:
      self.head=newnode
    else:
      ptr=self.head
      while ptr.next:
        ptr=ptr.next
      ptr.next=newnode
  def display(self):
    ptr=self.head
    while ptr:
      print(ptr.data,end=" ")
      ptr=ptr.next
  def deletelast(self):
    ptr=self.head
    while ptr.next.next is not None:
      ptr=ptr.next
    ptr.next=None

  def deletelastoldlogic(self):
    ptr=self.head
    while ptr.next is not None:
      prev=ptr
      ptr=ptr.next

    prev.next=None


l1=Linkedlist()
l1.create(91)
l1.create(34)
l1.create(3)
l1.display()
print("After delte last node")
#l1.deletelast()
l1.deletelastoldlogic()
l1.display()