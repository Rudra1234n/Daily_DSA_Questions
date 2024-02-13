'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
        '''
class Solution:
    def dfs(self, root, ans, rt):
        if not root:
            return float('-inf')

        l = self.dfs(root.left, ans, rt)
        r = self.dfs(root.right, ans, rt)

        if root == rt:
            l = 0 if l == float('-inf') else l
            r = 0 if r == float('-inf') else r
            ans[0] = max(ans[0], l + root.data + r)
        elif root.left and root.right:
            ans[0] = max(ans[0], l + root.data + r)
        return root.data + (0 if max(l, r) == float('-inf') else max(l, r))

    def maxPathSum(self, root):
        ans = [float('-inf')]
        self.dfs(root, ans, root)
        return ans[0]
