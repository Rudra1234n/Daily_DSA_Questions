# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
        
class Solution:
    def __init__(self):
        self.sum = float('-inf')
    
    def findMaxPathSum(self, root):
        if not root:
            return 0
        lsum = self.findMaxPathSum(root.left)
        rsum = self.findMaxPathSum(root.right)
        if not root.left and not root.right:
            return root.data
        if not root.left:
            return root.data + rsum
        if not root.right:
            return root.data + lsum
        self.sum = max(self.sum, root.data + lsum + rsum)
        return max(root.data + lsum, root.data + rsum)
    
    def maxPathSum(self, root):
        ans = self.findMaxPathSum(root)
        if not root.left or not root.right:
            self.sum = max(self.sum, ans)
        return self.sum
