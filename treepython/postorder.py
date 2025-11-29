class Node:
  def __init__(self,data):
    self.data=data
    self.left=None
    self.right=None

def insert(root,x):
  if root is None:
    return Node(x)
  else:
    if x<root.data:
      root.left=insert(root.left,x)
    else:
      root.right=insert(root.right,x)
  return root

def inorder(root):
  if root:
    inorder(root.left)
    print(root.data,end=" ")
    inorder(root.right)

root=None
n=3
for i in range (n):
  x=int(input("Enter Values:"))
  root=insert(root,x)
inorder(root)