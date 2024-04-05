class Solution:
    def correctBST(self, root):
        def inorder_traversal(node):
            if not node:
                return []
            return inorder_traversal(node.left) + [node] + inorder_traversal(node.right)
        
        nodes = inorder_traversal(root)
        
        first, second = None, None
        for i in range(len(nodes) - 1):
            if nodes[i].data > nodes[i + 1].data:
                if first is None:
                    first = nodes[i]
                second = nodes[i + 1]
        
        first.data, second.data = second.data, first.data
        
        return root

