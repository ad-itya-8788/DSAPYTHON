class Stack:
  def __init__(self):
    self.stack=[]
  def push(self,data):
    self.stack.append(data)
  def display(self):
    print(self.stack)
  def peek(self):
    print("Peek Element of Stack:",self.stack[-1])
x=Stack()
x.push(1)
x.push(3)
x.push(4)
x.display()
x.peek()