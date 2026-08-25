def is_balanced (root):
    def check (node):
        if not node :
            return 0
        
        left = check(node.left)
        if left == -1:
          return -1
        right =check(node .right)
        if right ==-1:
            return -1
        
        return 1 +max (right,left)
    return check(root) != -1
    

    
