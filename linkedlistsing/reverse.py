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
      print(ptr.data,end="->")
      ptr=ptr.next
    print("None")
  def reverse(self):
    curr=self.head
    next=None
    prev=None
    while curr:
      next=curr.next
      curr.next=prev
      prev=curr
      curr=next
    self.head=prev
l1=Linkedlist()
l1.create(1)
l1.create(2)
l1.create(3)
l1.create(4)
l1.display()
l1.reverse()
l1.display()