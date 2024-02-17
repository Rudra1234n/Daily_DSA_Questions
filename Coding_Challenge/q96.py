class Solution:
    def buildtree(self, inorder, preorder, n):
        def search(inorder, l, r, val):
            for i in range(l, r + 1):
                if inorder[i] == val:
                    return i
            return -1

        def cal(inorder, preorder, l, r):
            nonlocal ind
            if l > r:
                return None

            ptr = Node(preorder[ind])
            ind += 1

            if l == r:
                ptr.left = None
                ptr.right = None
                return ptr

            inindex = search(inorder, l, r, ptr.data)
            ptr.left = cal(inorder, preorder, l, inindex - 1)
            ptr.right = cal(inorder, preorder, inindex + 1, r)

            return ptr

        ind = 0
        return cal(inorder, preorder, 0, n - 1)
