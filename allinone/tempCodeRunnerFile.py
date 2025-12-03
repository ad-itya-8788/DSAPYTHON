class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
class clist:
  def __init__(self):
    self.head=None
  def add(self,data):
    newnode=Node(data)
    if self.head is None:
      self.head=newnode
      newnode.next=self.head
    else:
      ptr=self.head
      while ptr.next!=self.head:
        ptr=ptr.next
      ptr.next=newnode
      newnode.next=self.head
  def display(self):
    ptr=self.head
    while True:
      print(ptr.data,end="->")
      ptr=ptr.next
      if ptr==self.head:
        break
x=clist()
x.add(1)
x.add(3)
x.add(5)
x.add(5)
x.display()
