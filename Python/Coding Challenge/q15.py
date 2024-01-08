class Solution:
    
    #Function to return a list of integers denoting the node 
    #values of both the BST in a sorted order.
    def ele_out(self,root,k):
        if not root:
            return
        k.append(root.data)
        self.ele_out(root.right,k)
        self.ele_out(root.left,k)
    def merge(self, root1, root2):
        #code here.
        l=[]
        self.ele_out(root1,l)
        self.ele_out(root2,l)
        return sorted(l)
