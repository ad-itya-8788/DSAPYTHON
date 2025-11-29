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
def findmin(root):
  if root is None:
    return 0
  else:
    while root.left:
      root=root.left
    return root.data
      

root=None
root=insert(root,10)
root=insert(root,5)
root=insert(root,6)

inorder(root)

print("Minimum element is:",findmin(root))