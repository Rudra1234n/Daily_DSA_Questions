def deleteNode(root, x):
    if root is None:
        return None
    if x<root.data:
        root.left=deleteNode(root.left,x)
    elif x>root.data:
        root.right=deleteNode(root.right,x)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        current = root.right
        while current.left:
            current = current.left
        root.data=current.data
        root.right=deleteNode(root.right,root.data)
    return root
