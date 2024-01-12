'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
        '''
class Solution:
    #Function to find the height of a binary tree.
    def height(self, root):
        h = 0
        if root == None:
            return 0
        l,r = self.height(root.left), self.height(root.right)
        h = max(l,r) + 1
        return h
        
