class Solution:
    # returns the inorder successor of the Node x in BST (rooted at 'root')
    def inorderSuccessor(self, root, x):
        # Code here
        def inorder(root,l):
            if root is None:
                return None
            inorder(root.left,l)
            l.append(root.data)
            inorder(root.right,l)
        
        l=[]
        a=inorder(root,l)
        if l.index(x.data)+1>len(l)-1:
            return Node(-1)
        else:
            return Node(l[l.index(x.data)+1])
            
