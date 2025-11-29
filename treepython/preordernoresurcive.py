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

def preorder(root):
  if root is None:
    return
  stack=[root]
  while stack:
    node=stack.pop()
    print(node.data,end=" ")
    if node.right:
      stack.append(node.right)
    if node.left:
      stack.append(node.left)

root = None
root = insert(root,45)
root = insert(root,23)
root = insert(root,34)
root = insert(root,90)

preorder(root)
