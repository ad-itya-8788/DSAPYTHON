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

  def search(self,z):
    ptr=self.head
    x=0
    while ptr:
      if ptr.data==z:
        x=1
        break
      else:
       ptr=ptr.next
    if x==0:
      print("Not Found")
    else:
      print("Found")

l=LinkedList()
l.create(1)
l.create(2)
l.create(3)
l.display()

x=int(input("Enter Node to search:"))
l.search(x)