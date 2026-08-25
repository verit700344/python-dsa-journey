class node:
    def __init__(val,self):
        self.val=val
        self.right=None
        self.left=None
def inorder (root):
    inorder(root.left)
    print(root.val,end="")
    inorder(root.right) 