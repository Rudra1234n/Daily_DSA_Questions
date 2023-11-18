class Solution:
    def isleaf(self, root):
        return not root.left and not root.right

    def addLeftBoundary(self, root, res):
        curr = root.left
        while curr:
            if not self.isleaf(curr):
                res.append(curr.data)
            if curr.left:
                curr = curr.left
            else:
                curr = curr.right

    def addRightBoundary(self, root, res):
        curr = root.right
        st=[]
        while curr:
            if not self.isleaf(curr):
                st.append(curr.data)
            if curr.right:
                curr = curr.right
            else:
                curr = curr.left
        res.extend(reversed(st))
    
    def addleaf(self, root, res):
        if self.isleaf(root):
            res.append(root.data)
        if root.left:
            self.addleaf(root.left, res)
        if root.right:
            self.addleaf(root.right, res)

    def printBoundaryView(self, root):
        res = []
        if root is None:
            return res
        if not self.isleaf(root):
            res.append(root.data)
        self.addLeftBoundary(root, res)
        self.addleaf(root, res)
        self.addRightBoundary(root, res)
        return res

