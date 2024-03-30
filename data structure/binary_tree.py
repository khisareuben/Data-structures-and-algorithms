class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def preordertra(self):
        print(self.val, end=" ")
        if self.left:
            self.left.preordertra()
        if self.right:
            self.right.preordertra()

    def indordertra(self):
        if self.left:
            self.left.indordertra()
        print(self.val, end=" ")
        if self.right:
            self.right.indordertra()

    def postordertra(self):
        if self.left:
            self.left.postordertra()
        if self.right:
            self.right.postordertra()
        print(self.val, end=" ")


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)

print("preordertra: ", end=" ")
root.preordertra()
print()
print("indordertra: ", end=" ")
root.indordertra()
print()
print("postordertra: ", end=" ")
root.postordertra()
print()
