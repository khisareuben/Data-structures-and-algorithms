# creating a linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

# cheking if the list is empty or not
    def is_empty(self):
        return self.head is None

# checking the size of the linked list
    def size(self):
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next

        return count

# add a node at the beginning of the list
    def add(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new

# adding a node at the end of the list
    def add_at_end(self, data):
        new = Node(data)
        current = self.head
        while current.next:
            current = current.next
        current.next = new

# adding a node at a specific position in the list
    def add_at_spec_pos(self, data, position):
        new = Node(data)
        current = self.head
        for i in range(1, position-1):
            current = current.next
        new.next = current.next
        current.next = new

# removing a node at the beginning of the list
    def remove(self):
        current = self.head
        self.head = current.next
        current.next = None

# removing a node at the end of the list
    def remove_at_end(self):
        prev = self.head
        current = self.head.next
        while current.next:
            current = current.next
            prev = prev.next
        prev.next = None

# removing a node at a specific position in the list
    def remove_at_spec_pos(self, position):
        prev = self.head
        current = self.head.next
        for i in range(1, position-1):
            current = current.next
            prev = prev.next
        prev.next = current.next
        current.next = None

# stores the data in the list in order to be printed in an organised manner
    def screen(self):
        nodes = []
        current = self.head
        while current:
            nodes.append("%s" % current.data)
            current = current.next
        return "-> ".join(nodes)

# calling the linked list(class and methods) and the functions involved
l = LinkedList()
l.add(5)
l.add(4)
l.add(3)
l.add(2)
l.remove_at_spec_pos(2)
print(l.is_empty())
print(l.size())
print(l.screen())


