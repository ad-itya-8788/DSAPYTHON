class Stack:
  def __init__(self):
    self.stack=[]
  def push(self,data):
    self.stack.append(data)
  def display(self):
    if self.stack is None:
      print("Stack is Empty")
    else:
      print(self.stack)
x=Stack()
x.push(11)
x.push(23)
x.push(67)
x.display()
