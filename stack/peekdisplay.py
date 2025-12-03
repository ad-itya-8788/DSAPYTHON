class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
class Stack:
  def __init__(self):
    self.top=None
  def push(self,data):
    newnode=Node(data)
    if self.top is  None:
      self.top=newnode
    else:
      newnode.next=self.top
      self.top=newnode
  def display(self):
    ptr=self.top
    while ptr:
      print(ptr.data,end=" ")
      ptr=ptr.next
  def peek(self):
    if self.top is None:
      return 0
    else:
      return self.top.data
x=Stack()
x.push(1)
x.push(3)
x.push(34)
x.display()
print("Top Element is :",x.peek())