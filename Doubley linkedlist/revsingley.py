class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
class slist:
  def __init__(self):
    self.head=None
  def insert(self,data):
    newnode=Node(data)
    if self.head is None:
      self.head=newnode
    else:
      ptr=self.head
      while ptr.next is not None:
        ptr=ptr.next
      ptr.next=newnode

  def display(self):
    ptr=self.head
    while ptr:
      print(ptr.data,end=" ")
      ptr=ptr.next


x=slist()
x.insert(1)
x.insert(2)
x.insert(3)
x.display()