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
    ptr=self.top
    while ptr:
      print(ptr.data,end="-->")
      ptr=ptr.next
  def peek(self):
    ptr=self.top
    print("Peek is:",ptr.data)
  def size(self):
    x=0
    ptr=self.top
    while ptr:
      ptr=ptr.next
      x+=1
    print("Size is :",x)
  def pop(self):
    self.top=self.top.next
  def reverse(self):
    temp_stack=Stack()
    while self.top:
      data=self.pop()
      temp_stack.push(data)
    self.top=temp_stack.top

x=Stack()
x.push(1)
x.push(2)
x.push(3)

x.display()
x.reverse()
print()
x.display()
