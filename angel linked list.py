# Struktur Data Tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Membuat tree
root = Node("A")
root.left = Node("B")
root.right = Node("C")
root.left.left = Node("D")
root.left.right = Node("E")

# Menampilkan isi tree (preorder traversal)
def preorder(node):
    if node:
        print(node.data)
        preorder(node.left)
        preorder(node.right)

print("Traversal Tree:")
preorder(root)