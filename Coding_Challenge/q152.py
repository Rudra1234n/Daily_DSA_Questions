class Solution:
    def solve(self, root):
        if not root:
            return [1, 0, float('inf'), float('-inf')]
        if root.left is None and root.right is None:
            return [1, 1, root.data, root.data]
        l = self.solve(root.left)
        r = self.solve(root.right)
        if l[0] and r[0]:
            if root.data > l[3] and root.data < r[2]:
                x = l[2] if l[2] != float('inf') else root.data
                y = r[3] if r[3] != float('-inf') else root.data
                return [1, l[1] + r[1] + 1, x, y]
        return [0, max(l[1], r[1]), 0, 0]

    def largestBst(self, root):
        ans = [0, 0, 0, 0]
        ans = self.solve(root)
        return ans[1]
