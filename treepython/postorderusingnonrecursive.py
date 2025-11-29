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

def postorder(root):
    if root is None:
        return

    s1 = []
    s2 = []

    s1.append(root)

    while s1:
        node = s1.pop()
        s2.append(node)

        if node.left:
            s1.append(node.left)
        if node.right:
            s1.append(node.right)

    while s2:
        print(s2.pop().data, end=" ")

root = None
root = insert(root,45)
root = insert(root,23)
root = insert(root,34)
root = insert(root,90)

postorder(root)
