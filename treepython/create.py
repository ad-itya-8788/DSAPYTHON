class Node:
  def __init__(self,data):
   self.data=data
   self.left=None
   self.right=None
  def inorder(self,node):
    if node:
      self.inorder(node.left)
      print(node.data,end=" ")
      self.inorder(node.right)

root=Node(10)
root.left=Node(5)
root.right=Node(15)
root.left.left=Node(4)
root.left.right=Node(3)
root.right.left=Node(10)
root.right.left=Node(23)

root.inorder(root)

print()