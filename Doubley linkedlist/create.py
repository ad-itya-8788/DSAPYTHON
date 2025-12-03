class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
    self.prev=None
class dlinkedlist:
  def __init__(self):
    self.head=None
  def create(self,data):
    nnode=Node(data)
    if self.head is None:
      self.head=nnode
    else:
      ptr=self.head
      while ptr.next is not None:
        ptr=ptr.next
      ptr.next=nnode
      nnode.prev=ptr
  def display(self):
    ptr=self.head
    while ptr:
      print(ptr.data,end="->")
      ptr=ptr.next
x=dlinkedlist()
x.create(12)
x.create(45)
x.create(34)
x.display()