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

  def display(self):
    ptr=self.head
    while ptr:
      print(ptr.data,end="->")
      ptr=ptr.next
    print("None")
  def addafter(self,x,y):
    ptr=self.head
    while ptr:
      if ptr.data==x:
        node=Node(y)
        node.next=ptr.next
        ptr.next=node
        break
      ptr=ptr.next


l1=LinkedList()
l1.create(1)
l1.create(2)
l1.create(3)
l1.display()
x=2
y=67
l1.addafter(x,y)
l1.display()