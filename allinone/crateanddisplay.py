class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DL:
    def __init__(self):
        self.head = None

    def add(self, data):      # Insert at end
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
        else:
            ptr = self.head
            while ptr.next:
                ptr = ptr.next
            ptr.next = newnode
            newnode.prev = ptr

    def display(self):
        ptr = self.head
        while ptr:
            print(ptr.data, end="<->")
            ptr = ptr.next
        print("None")
    def addbf(self,x,y):
        ptr=self.head
        newnode=Node(x)
        while ptr and ptr.data!=x:
            ptr=ptr.next
        newnode.next=ptr
        newnode.prev=ptr.prev
        ptr.prev.next=newnode
        ptr.prev=newnode
x = DL()
x.add(10)
x.add(20)
x.add(30)
x.add(40)


x.display()
x.addbf(99,30)