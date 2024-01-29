class Solution:
    def is_sum(self, root):
        if root is None:
            return 0
            
        left = self.is_sum(root.left) + root.left.data if root.left else 0
        right = self.is_sum(root.right) + root.right.data if root.right else 0
        if left+right != root.data and root.left and root.right:
            return float("-inf")
        return left + right
        
    def isSumTree(self,root):
        # Code here
        if root.left is None and root.right is None:
            return 1
        ans = self.is_sum(root)
        if ans==float("-inf") or ans!=root.data:
            return 0
        
        return 1
