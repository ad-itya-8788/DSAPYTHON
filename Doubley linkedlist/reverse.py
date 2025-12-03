class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
    self.prev=None
class dlinkedlist:
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
      newnode.prev=ptr
  def display(self):
    ptr=self.head
    while ptr:
      print(ptr.data,end=" ->")
      ptr=ptr.next
    print("None")
  def reverse(self):
    ptr=self.head
    while ptr.next is not None:
      ptr=ptr.next
    while ptr is not None:
      print(ptr.data,end="<--")
      ptr=ptr.prev
  def deletehead(self):
    self.head=self.head.next
  def addfirst(self,z):
    newnode=Node(z)
    newnode.next=self.head
    self.head=newnode
  def addafter(self,curr,add):
    ptr=self.head
    newnode=Node(add)
    while ptr.data!=curr:
      ptr=ptr.next
    newnode.next=ptr.next
    newnode.prev=ptr
    if ptr.next:
      ptr.next.prev=newnode
    ptr.next=newnode
x=dlinkedlist()
x.insert(12)
x.insert(34)
x.insert(67)
x.display()
x.reverse()

x.deletehead()
print()
x.display()
x.addfirst(90)
x.display()

x.addafter(34,89)
x.display()