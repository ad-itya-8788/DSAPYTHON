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
def preorder(root):
  stack=[root]
  while stack:
    curr=stack.pop()
    print(curr.data,end=" ")
    if curr.right:
      stack.append(curr.right)
    if curr.left:
      stack.append(curr.left)
def inorder(root):
  stack=[]
  curr=root
  while curr or stack:
    while curr:
      stack.append(curr)
      curr=curr.left
    curr=stack.pop()
    print(curr.data,end=" ")
    curr=curr.right
root=None
root=add(root,3)
root=add(root,5)
root=add(root,2)
postorder(root)
preorder(root)
inorder(root)