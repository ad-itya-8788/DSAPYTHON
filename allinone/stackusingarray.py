stack=[]
def push(x):
  stack.append(x)
def pop():
  stack.pop()
def peek():
  print("Peek is:",stack[-1])
def size():
  print("size of stack is:",len(stack))
def display():
  print("Display Stack:",stack)
push(1)
push(3)
push(5)
display()
pop()
display()
size()
peek()
