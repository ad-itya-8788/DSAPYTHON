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
def preorder(root):
  if root:
    print(root.data,end=" ")
    preorder(root.left)
    preorder(root.right)

def display(root):
  if root is None:
    return root
  stack=[root]
  while stack:
    curr=stack.pop()
    print(curr.data,end=" ")
    if curr.right:
      stack.append(curr.right)
    if curr.left:
      stack.append(curr.left)
root=None
root=add(root,11)
root=add(root,4)
root=add(root,5)
root=add(root,9)

preorder(root)
display(root)