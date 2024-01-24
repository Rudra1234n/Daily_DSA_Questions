class Solution:
    def isSymmetric(self, root):
        def helper(l,r):
            if not l and not r:
                return True
            if (not l and r) or (not r and l) or (l and r and l.data!=r.data ):
                return False
            return helper(l.left, r.right) and helper(l.right, r.left)
        return helper(root.left, root.right) if root else True
