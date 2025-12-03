class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CLL:
    def __init__(self):
        self.head = None

    # INSERT AT END
    def add(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
            new.next = self.head
        else:
            ptr = self.head
            while ptr.next != self.head:
                ptr = ptr.next
            ptr.next = new
            new.next = self.head

    # INSERT AFTER X
    def addafter(self, x, y):
        ptr = self.head
        new = Node(y)
        while ptr.data != x:
            ptr = ptr.next
        new.next = ptr.next
        ptr.next = new

    # INSERT BEFORE X
    def addbefore(self, x, y):
        new = Node(y)
        ptr = self.head
        prev = None
        while ptr.data != x:
            prev = ptr
            ptr = ptr.next
        new.next = ptr
        prev.next = new

    # REVERSE CIRCULAR LIST
    def reverse(self):
        prev = None
        curr = self.head
        start = self.head

        while True:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            if curr == start:
                break

        start.next = prev
        self.head = prev

    # DISPLAY CIRCULAR LIST
    def display(self):
        ptr = self.head
        while True:
            print(ptr.data, end="->")
            ptr = ptr.next
            if ptr == self.head:
                break
        print()
x = CLL()
x.add(10)
x.add(20)
x.add(30)
x.add(40)

print("Original:")
x.display()

x.addafter(20, 99)
print("After addafter(20,99):")
x.display()

x.addbefore(30, 555)
print("After addbefore(30,555):")
x.display()

x.reverse()
print("After reverse:")
x.display()
