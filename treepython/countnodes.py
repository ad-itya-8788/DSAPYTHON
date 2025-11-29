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
def count(root):
  if root is None:
    return 0
  else:
    return count(root.left)+count(root.right)+1
root=None
root=insert(root,45)
root=insert(root,12)
root=insert(root,90)
inorder(root)
print("Count is:",count(root))
