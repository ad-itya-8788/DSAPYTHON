class Stack:
  def __init__(self):
    self.stack=[]
  def push(self,data):
    self.stack.append(data)
  def display(self):
    print("Stack is:",self.stack)
  def pop(self):
    x=self.stack[-1]
    print("Element is poped",x)
    self.stack.pop()
x=Stack()
x.push(1)
x.push(2)
x.push(3)
x.push(4)
x.display()
x.pop()
x.display()