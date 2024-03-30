class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Dll:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def forward_traversal(self):
        print()
        if self.head is None:
            print("List is empty")
        else:
            current = self.head
            while current:
                print(current.data, end=" ")
                current = current.next
    
    def backward_traversal(self):
        print()
        if self.head is None:
            print("List is empty")
        else:
            current = self.head
            while current.next:
                current = current.next
            while current:
                print(current.data, end=" ")
                current = current.prev

    def insert_at_begin(self, data):
        new = Node(data)
        current = self.head
        current.prev = new
        new.next = current
        self.head = new

    def insert_at_end(self, data):
        new = Node(data)
        current = self.head
        while current.next:
            current = current.next
        current.next = new
        new.prev = current

    def insert_at_spec_pos(self, data, position):
        new = Node(data)
        current = self.head
        for i in range(1, position-1):
            current = current.next
        new.prev = current
        new.next = current.next
        new.next.prev = new
        current.next = new

    def del_at_begin(self):
        current = self.head
        self.head = current.next
        self.head.prev = None
        current.next = None
    
    def del_at_end(self):
        before = self.head
        current = self.head.next
        while current.next:
            current = current.next
            before = before.next
        before.next = None
        current.prev = None

    def del_at_spec_pos(self):
        before = self.head
        current = self.head.next
        while current:
            current = current.next
            before = before.next
        before.next = current.next
        current.prev = None
        current.next.prev = before
        current.next = None

n1 = Node(5)
dll = Dll()
dll.head = n1
n2 = Node(10)
n2.prev = n1
n1.next = n2
n3 = Node(15)
n3.prev = n2
n2.next = n3
n4 = Node(20)
n4.prev = n3
n3.next = n4
dll.insert_at_begin(2)
dll.forward_traversal()
dll.backward_traversal()

