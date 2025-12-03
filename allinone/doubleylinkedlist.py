class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class dl:
    def __init__(self):
        self.head = None

    # INSERT AT END
    def add(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
        else:
            ptr = self.head
            while ptr.next:
                ptr = ptr.next
            ptr.next = newnode
            newnode.prev = ptr

    # DISPLAY FORWARD
    def display(self):
        ptr = self.head
        while ptr:
            print(ptr.data, end=" <-> ")
            ptr = ptr.next
        print("None")

    # DISPLAY REVERSE
    def reverse(self):
        ptr = self.head
        if ptr is None:
            return
        while ptr.next:
            ptr = ptr.next
        while ptr:
            print(ptr.data, end=" <-> ")
            ptr = ptr.prev
        print("None")

    # INSERT AT FIRST
    def addfirst(self, data):
        newnode = Node(data)
        newnode.next = self.head
        if self.head:
            self.head.prev = newnode
        self.head = newnode

    # INSERT AFTER VALUE x
    def addafter(self, x, y):
        ptr = self.head
        while ptr and ptr.data != x:
            ptr = ptr.next
        if ptr is None:
            print("Value not found")
            return

        newnode = Node(y)
        newnode.prev = ptr
        newnode.next = ptr.next

        if ptr.next:
            ptr.next.prev = newnode

        ptr.next = newnode

    # INSERT BEFORE VALUE x
    def addbefore(self, x, y):
        ptr = self.head
        while ptr and ptr.data != x:
            ptr = ptr.next
        if ptr is None:
            print("Value not found")
            return

        newnode = Node(y)

        # If inserting before head
        if ptr.prev is None:
            newnode.next = self.head
            self.head.prev = newnode
            self.head = newnode
            return

        newnode.prev = ptr.prev
        newnode.next = ptr

        ptr.prev.next = newnode
        ptr.prev = newnode

    # DELETE VALUE
    def remove(self, x):
        ptr = self.head

        # find
        while ptr and ptr.data != x:
            ptr = ptr.next
        if ptr is None:
            print("Value not found")
            return

        # delete first
        if ptr.prev is None:
            self.head = ptr.next
            if self.head:
                self.head.prev = None
            return

        # delete last
        if ptr.next is None:
            ptr.prev.next = None
            return

        # delete middle
        ptr.prev.next = ptr.next
        ptr.next.prev = ptr.prev
x = dl()
x.add(2)
x.add(4)
x.add(5)
x.add(67)

print("Forward:")
x.display()

print("Reverse:")
x.reverse()

print("Add First 90:")
x.addfirst(90)
x.display()

print("Add After 4 -> 89")
x.addafter(4, 89)
x.display()

print("Add Before 5 -> 999")
x.addbefore(5, 999)
x.display()

print("Remove 4:")
x.remove(4)
x.display()
