#User function Template for python3
class Node:
    def __init__(self,  data):
        self.data = data
        self.left = None
        self.right = None
class Solution:
    def insert(self,root, Key):
        if root == None:
            return Node(Key)
        elif root.data > Key:
            root.left  = self.insert(root.left , Key)
        else:
            root.right = self.insert(root.right , Key)
        return root
