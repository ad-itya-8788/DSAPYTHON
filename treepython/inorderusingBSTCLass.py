class Node:
  def __init__(self,data):
    self.data=data
    self.left=None
    self.right=None
class BST:
  def __init__(self):
    self.root=None
  def insert(self,x):
    self.root=self._insert(self.root,x)
  def _insert(self,root,x):
    if root is None:
      return Node(x)
    if x<root.data:
      root.left=self._insert(root.left,x)
    else:
      root.right=self._insert(root.right,x)
    return root
  def inorder(self):
    self._inorder(self.root)
    print()
  def _inorder(self,root):
    if root:
      self._inorder(root.left)
      print(root.data,end=" ")
      self._inorder(root.right)


tree = BST()
tree.insert(10)
tree.insert(5)
tree.insert(20)
tree.insert(15)

tree.inorder()
