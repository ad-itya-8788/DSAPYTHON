class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
    
class LinkedList:
  def __init__(self):
    self.head=None
  def create(self,data):
    node=Node(data)
    if self.head is None:
      self.head=node
    else:
      ptr=self.head
      while ptr.next:
        ptr=ptr.next
      ptr.next=node

  def addStart(self,data):
    node=Node(data)
    node.next=self.head
    self.head=node

  def display(self):
    ptr=self.head
    while ptr:
      print(ptr.data,end="->")
      ptr=ptr.next
    print("None")

l=LinkedList()
l.create(10)
l.create(30)
l.create(3)
l.display()

l.addStart(343)
l.display()