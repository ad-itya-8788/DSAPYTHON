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
def preorder(root):
  if root:
    print(root.data)
    preorder(root.left)
    preorder(root.right)
def countNodes(root):
  if root is None:
    return 0
  else:
    return countNodes(root.left)+countNodes(root.right)+1
n=4
root=None
for i in range( n):
  x=int(input("Enter Data:"))
  root=insert(root,x)

preorder(root)
print("Total Nodes:",countNodes(root))
