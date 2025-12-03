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
    curr=self.top
    prev=None
    while curr:
      next=curr.next
      curr.next=prev
      prev=curr
      curr=next
    self.top=prev

x=Stack()
x.push(1)
x.push(2)
x.push(3)

x.display()
x.reverse()
print()
x.display()
