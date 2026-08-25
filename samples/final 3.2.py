def height(root):
    if not root:
        return 0
    return 1 +max (height(root.right),(height(root.left)))