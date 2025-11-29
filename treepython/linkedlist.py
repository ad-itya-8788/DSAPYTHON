class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
class linkedlist:
  def __init__(self):
    self.head=None
  def create(self,data):
    newnode=Node(data)
    if self.head is None:
      self.head=newnode
    else:
      ptr=self.head
      while ptr.next is not None:
        ptr=ptr.next
      ptr.next=newnode
  def display(self):
    ptr=self.head
    while ptr:
      print(ptr.data,end="->")
      ptr=ptr.next
    print("None")
  def reverse(self):
    prev=None
    curr=self.head
    while curr:
      next=curr.next
      curr.next=prev
      prev=curr
      curr=next
    self.head=prev

x=linkedlist()
x.create(1)
x.create(2)
x.create(3)
print("Display Linkedlist:-")
x.display()
print("Linked lis in Reverse Order:-")
x.reverse()
x.display()