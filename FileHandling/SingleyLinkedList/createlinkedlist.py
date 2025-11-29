class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def add(self, data):
        newnode = Node(data)
        if self.head == None:
            self.head = newnode
        else:
            ptr = self.head
            while ptr.next != None:
                ptr = ptr.next
            ptr.next = newnode

    def display(self):
        ptr = self.head
        while ptr:
            print(ptr.data, end="->")
            ptr = ptr.next

    def addbg(self, data):
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode

    def addafter(self, x, y):
        ptr = self.head
        while ptr.data != y:
            ptr = ptr.next
        newnode = Node(x)
        newnode.next = ptr.next
        ptr.next = newnode


l1 = Linkedlist()
l1.add(1)
l1.add(334)
l1.add(3443)
l1.display()
print("\nAfter Adding New node at first")
l1.addbg(23)
l1.display()
x, y = map(int, input("\n Add x after y:").split())
l1.addafter(x, y)
l1.display()
