class Solution:        
    def __init__(self):
        self.res = -1*(2**63 - 1)
    def s(self, root, ischild):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return root.data
        
        l = self.s(root.left, True)
        r = self.s(root.right, True)
        temp = root.data+l+r
        if root.left is None:
            l = -1*(2**63 - 1)
        if root.right is None:
            r = -1*(2**63 - 1)
        
        
        ans = max(l,r) + root.data
        if root.left is not None and root.right is not None or ischild == False:
            self.res = max(self.res,  temp)
        return ans
        
    def maxPathSum(self, root):
        # code here
        self.s(root, False)
        return self.res
