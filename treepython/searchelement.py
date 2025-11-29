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
    print(root.data,end=" ")
    inorder(root.left)
    inorder(root.right)
def find(root,x):
  if root is None:
    return 0
  if root.data==x:
    return 1
  if x<root.data:
    return find(root.left,x)
  else:
    return find(root.right,x)

root=None
root=insert(root,45)
root=insert(root,23)
root=insert(root,34)
inorder(root)
if(find(root,364)):
 print("Element is present in Tree")
else:
  print("Element is Not present in Tree")