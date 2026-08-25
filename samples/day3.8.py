class treenode:
    def __init__(self,val=0,left= None,right=None):
        self.val=val
        self.right=right
        self.left=left



def is_balanced(root):
    def check (node):
        if not node:
            return 0
        left= check(node.left)
        if left == -1:
            return -1
        right=check(node.right)
        if right == -1:
            return -1
        if abs(left - right) > 1:
            return -1   
        return max(left, right) + 1
    
    return check(root) != -1

root=treenode(3)
root.right=treenode(9)
root.left=treenode(9)

print(is_balanced(root))

unbalanced_root=treenode(2)
unbalanced_root.left=treenode(3)
unbalanced_root.right=treenode(5)   
print(is_balanced(unbalanced_root))