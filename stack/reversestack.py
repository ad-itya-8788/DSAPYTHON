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
      print(ptr.data,end=" ")
      ptr=ptr.next
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
x.push(3)
x.push(34)
x.display()
x.reverse()
print("\nStack After Reverse:")
x.display()