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
def postorder(root):
  if root:
    postorder(root.right)
    print(root.data)
    postorder(root.left)
def display(root):
  s1=[]
  s2=[]
  ptr=root
  s1.append(root)
  while s1:
    curr=s1.pop()
    if curr.left:
      s1.append(root.left)
    if curr.right:
      s1.append(root.right)
    while s2:
      print(s2.pop(),end=" ")
root=None
root=add(root,2)
root=add(root,1)
root=add(root,34)
postorder(root)
display(root)