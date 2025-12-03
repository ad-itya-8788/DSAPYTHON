class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
class Stack:
  def __init__(self):
    self.rear=None
    self.front=None
  def enqueu(self,data):
    newnode=Node(data)
    if self.front is None:
      self.front=self.rear=newnode
    self.rear.next=newnode
    self.rear=newnode
  def display(self):
    ptr=self.front
    while ptr:
      print(ptr.data,end=" ")
      ptr=ptr.next
  def rev(self):
    curr=self.front
    prev=None
    self.rear=curr
    while curr:
      next=curr.next
      curr.next=prev
      prev=curr
      curr=next
    self.front=prev
x=Stack()
x.enqueu(12)
x.enqueu(34)
x.enqueu(56)
x.display()
x.rev()
print("Queue After Reverse:")
x.display()