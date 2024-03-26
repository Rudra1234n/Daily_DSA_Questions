
'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    def KthSmallestElement(self, root, k): 
        count=1
        while root:
            if not root.left:
                if count==k:
                    return root.data
                else:
                    count+=1
                root=root.right
            else:
                prev=root.left
                while prev.right and prev.right!=root:
                    prev=prev.right
                if prev.right==None:
                    prev.right = root
                    root=root.left
                else:
                    prev.right=None
                    if count==k:
                        return root.data
                    else:
                        count+=1
                    root=root.right
        return -1
