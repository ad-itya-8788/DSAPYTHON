class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def add(root,data):
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = add(root.left, data)
    else:
        root.right = add(root.right, data)
    return root

def find_min(root):
    if root is None:
        return None
    curr = root
    while curr.left:
        curr = curr.left
    return curr.data

def find_max(root):
    if root is None:
        return None
    curr = root
    while curr.right:
        curr = curr.right
    return curr.data

def search(root, key):
    if root is None:
        return False
    if root.data == key:
        return True
    elif key < root.data:
        return search(root.left, key)
    else:
        return search(root.right, key)

def count_nodes(root):
    if root is None:
        return 0
    return count_nodes(root.left) + count_nodes(root.right) + 1


# Test
root=None
root=add(root,10)
root=add(root,5)
root=add(root,15)
root=add(root,12)
root=add(root,18)

print("Min:", find_min(root))
print("Max:", find_max(root))
print("Search 12:", search(root,12))
print("Search 99:", search(root,99))
print("Count:", count_nodes(root))
