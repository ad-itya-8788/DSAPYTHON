class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
class Stack:
  def __init__(self):
    self.rear=None
    self.front=None
  def enque(self,data):
    newnode=Node(data)
    if self.front is None:
      self.rear=self.front=newnode
    self.rear.next=newnode
    self.rear=newnode
  def display(self):
    if self.front is None:
      print("Queue is Empty")
      return
    ptr=self.front
    while ptr:
      print(ptr.data,end=" ")
      ptr=ptr.next
  def dequeu(self):
    if self.front is None:
      print("Queue is Empty")
    else:
      self.front=self.front.next
x=Stack()
x.enque(1)
x.enque(2)
x.enque(3)
x.display()
x.dequeu()
print("After Equeue:")
x.display()