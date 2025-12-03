class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
class Queue:
  def __init__(self):
    self.front=self.rear=None
  def add(self,data):
    newnode=Node(data)
    if self.front is None:
      self.front=self.rear=newnode
    else:
      self.rear.next=newnode
      self.rear=newnode
  def display(self):
    ptr=self.front
    while ptr:
      print(ptr.data,end=" ")
      ptr=ptr.next
  def enque(self):
    self.front=self.front.next
  def reverse(self):
    stack=[]
    ptr=self.front
    while ptr:
      stack.append(ptr.data)
      ptr=ptr.next
    self.front=self.rear=None

    for data in stack[::-1]:
      self.add(data)


x=Queue()
x.add(1)
x.add(2)
x.add(3)
x.add(4)
x.add(5)
x.add(6)

x.display()

x.enque()
print()
x.display()
x.reverse()
print()
x.display()
