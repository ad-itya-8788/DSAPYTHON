class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None

class dl:
  def __init__(self):
    self.head = None

  def create(self, data):
    nn = Node(data)
    if self.head is None:
      self.head = nn
    else:
      ptr = self.head
      while ptr.next is not None:
        ptr = ptr.next
      ptr.next = nn
      nn.prev = ptr

  def display(self):
    ptr = self.head
    while ptr:
      print(ptr.data, end="->")
      ptr = ptr.next
    print("None")
  def deletefist(self):
    ptr=self.head.next
    self.head=ptr

x = dl()
x.create(1)
x.create(2)
x.create(3)
x.display()
x.deletefist()
x.display()
