class Stack:
  def __init__(self):
    self.stack=[]
  def push(self,data):
    self.stack.append(data)
  def display(self):
    print(self.stack)
  def reverse(self):
    rev=[]
    while self.stack:
      rev.append(self.stack.pop())
    return rev
s=Stack()
s.push(1)
s.push(3)
s.push(4)
s.display()
print("Stack After Reverese:",s.reverse())