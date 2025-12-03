class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
class Queue:
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
    if self.front is None:
      print("Queue is Empty")
      return
    else:
      ptr=self.front
      while ptr:
        print(ptr.data,end=" ")
        ptr=ptr.next
      print("None")
x=Queue()
x.enqueu(1)
x.enqueu(2)
x.enqueu(3)
x.display()