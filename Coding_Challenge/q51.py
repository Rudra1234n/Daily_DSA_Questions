class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class Solution:
    #Function to insert a node in a BST. 
    def insert(self,root, key):
        # code here
        if root is None:
            return Node(key)
        parent = None
        curr =root
        while curr != None:
            parent = curr
            if curr.data == key:
                return root
            elif curr.data > key:
                curr = curr.left
            else:
                curr = curr.right
        
        if parent.data > key:
            parent.left=Node(key)
        else:
            parent.right = Node(key)
        return root
