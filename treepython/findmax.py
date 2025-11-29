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
def postorder(root):
  if root:
    postorder(root.right)
    postorder(root.left)
    print(root.data,end=" ")
def findmax(root):
  if root is None:
    return 0
  else:
    while root.right:
      root=root.right
    return root.data

root=None
root=insert(root,10)
root=insert(root,5)
root=insert(root,90)
postorder(root)

print("Max is:",findmax(root))