def kthAncestor(root, k, node):
    # Helper function to build the parent dictionary
    def preorder(root, parent):
        if root is None:
            return
        if root.left is not None:
            parent[root.left.data] = root 
            preorder(root.left, parent)
        if root.right is not None:
            parent[root.right.data] = root 
            preorder(root.right, parent)

    parent = {}
    preorder(root, parent)

    curr = node
    while k > 0 and curr in parent:
        curr = parent[curr].data
        k -= 1

    return curr if k == 0 else -1
