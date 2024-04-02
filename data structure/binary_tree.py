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

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)

print("preorder: ", end=" ")
root.preorder(root)
print()
print("inorder: ", end=" ")
root.inorder(root)
print()
print("postorder: ", end=" ")
root.postorder(root)
