class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, x):
    if root is None:
        return Node(x)
    else:
        if x < root.data:
            root.left = insert(root.left, x)
        else:
            root.right = insert(root.right, x)
        return root

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
root = None
root = insert(root,45)
root = insert(root,23)
root = insert(root,34)
root=insert(root,90)

inorder(root)
