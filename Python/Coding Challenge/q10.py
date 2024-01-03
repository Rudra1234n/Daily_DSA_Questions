class Solution:
    
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    def topView(self,root):
        if root is None:
            return []

        queue = []
        hdMap = {}
        hd = 0

        queue.append((root, hd))

        while queue:
            node, hd = queue.pop(0)

            if hd not in hdMap:
                hdMap[hd] = node.data

            if node.left:
                queue.append((node.left, hd - 1))

            if node.right:
                queue.append((node.right, hd + 1))

        result = []
        for hd in sorted(hdMap.keys()):
            result.append(hdMap[hd])

        return result
