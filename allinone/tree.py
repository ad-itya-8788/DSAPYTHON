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
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)
def display(root):
  curr=root
  stack=[]
  while curr or stack:
    while curr:
      stack.append(curr)
      curr=curr.left
    curr=stack.pop()
    print(curr.data,end=" ")
    curr=curr.right
root=None
root=add(root,1)
root=add(root,2)
root=add(root,3)
root=add(root,4)
root=add(root,5)
root=add(root,6)
inorder(root)
display(root)