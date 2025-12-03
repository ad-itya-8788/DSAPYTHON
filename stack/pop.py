class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
class Stack:
  def __init__(self):
    self.top=None
  def push(self,data):
    newnode=Node(data)
    if self.top is None:
      self.top=newnode
    else:
      newnode.next=self.top
      self.top=newnode
  def display(self):
    if self.top is None:
      print("Stack is Empty")
    else:
      ptr=self.top
      while ptr:
        print(ptr.data,end=" ")
        ptr=ptr.next
      print("None")
  def pop(self):
    if self.top is None:
      print("Stack is Empty")
    else:
      z=self.top.next
      self.top=z

x=Stack()
x.push(34)
x.push(23)
x.push(1)
x.display()
x.pop()
x.display()
