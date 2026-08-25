class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None       

def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder(root): 
     if root: 
          inorder(root.left) 
          print(root.data, end=" ") 
          inorder(root.right)   


def max_h(root):
        if not root:
           return 0
        return 1 + max(max_h(root.left), max_h(root.right))

root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.right = Node(15)
root.left.left = Node(2)
root.left.right = Node(7)

print(max_h(root))  # Output: 3
print("Inorder traversal of tree:") 
inorder(root)