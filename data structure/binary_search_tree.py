class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def visit(self, node):
        print(node.val, end=" ")

    def preorder(self, current):
        if current is None:
            return 
        self.visit(current)
        self.preorder(current.left)
        self.preorder(current.right)

    def inorder(self, current):
        if current is None:
            return 
        self.inorder(current.left)
        self.visit(current)
        self.inorder(current.right)

    def postorder(self, current):
        if current is None:
            return 
        self.postorder(current.left)
        self.postorder(current.right)
        self.visit(current)

    def insert(self, data):
        if self.val:
            if data < self.val:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)

            elif data > self.val:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)

        else:
            self.val = data

    def search(self, key):
        if key < self.val:
            if self.left is None:
                return str(key) + " Not found"
            else:
                return self.left.search(key)
        elif key > self.val:
            if self.right is None:
                return str(key) + " Not found"
            else:
                return self.right.search(key)
        else:
            return str(key) + " is found"

root = Node(50)
root.insert(30)
root.insert(20)
root.insert(40)
root.insert(70)
root.insert(60)
root.insert(80)

print(root.search(60))
print(root.search(100))

print("preorder: ", end=" ")
root.preorder(root)
print()
print("inorder: ", end=" ")
root.preorder(root)
print()
print("postorder: ", end=" ")
root.postorder(root)
