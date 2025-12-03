class Node:
  def __init__(self,data):
    self.data=data
    self.left=None
    self.right=None
def add(root,data):
  newnode=Node(data)
  if root is None:
    return Node(data)
  else:
    if data<root.data:
      root.left=add(root.left,data)
    else:
      root.right=add(root.right,data)
  return root
def display(root):
  curr=root
  s1=[]
  s2=[]
  s1.append(root)
  while s1:
    curr=s1.pop()
    s2.append(curr)
    if curr.left:
      s1.append(curr.left)
    if curr.right:
      s1.append(curr.right)
  while s2:
    print(s2.pop().data,end=" ")
root=None
root=add(root,10)
root=add(root,13)
root=add(root,56)

display(root)