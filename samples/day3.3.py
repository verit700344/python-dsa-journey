def identical(r1,r2):
    if r1 and r2 == None:
        return True
    if r1 == None or r2 == None:
        return False    
    return(
        r1.val==r2.val and identical(r1.left,r1.right) and identical(r2.right,r2.left)
    )
