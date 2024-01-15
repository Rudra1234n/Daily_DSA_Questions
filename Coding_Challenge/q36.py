def findSpiral(root):
    # Code here
    
    res = []
    if not root:
        return res
    
    stk1 = [] # store left to right
    stk2 = [] # store right to left
    stk1.append(root) 
    
    while stk1 or stk2:
        while stk1:
            node = stk1.pop()
            res.append(node.data)
            
            if node.right:
                stk2.append(node.right)
            
            if node.left:
                stk2.append(node.left)
        
        while stk2:
            node = stk2.pop()
            res.append(node.data)
            
            if node.left:
                stk1.append(node.left)
            
            if node.right:
                stk1.append(node.right)
                
    return res
