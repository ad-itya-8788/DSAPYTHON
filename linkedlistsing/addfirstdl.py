class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
    self.prev=None
    
class dl:
  def __init__(self):
    self.head=None
  def create(self,data):
    newnode=Node(data)
    if self.head is None:
      self.head=newnode
    else:
      ptr=self.head
      while ptr.next is not None:
        ptr=ptr.next
      ptr.next=newnode
      newnode.prev=ptr
  def display(self):
    ptr=self.head
    while ptr:
      print(ptr.data,end="->")
      ptr=ptr.next
    print("None")
  def addfist(self,data):
    newnode=Node(data)
    if self.head is None:
      self.head=newnode
    else:
      ptr=self.head
      newnode.next=ptr
      self.head.prev=newnode
      self.head=newnode
x=dl()
x.create(1)
x.create(2)
x.create(3)
x.create(4)
x.display()
x.addfist(23)
x.display()