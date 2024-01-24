class Solution:
    def kthLargest(self,root, k):
        
        temp=[]
        
        if root==None:
            return None
            
        
        def check(root,temp):
            
            if root:
                temp.append(root.data)
                check(root.left,temp)
                check(root.right,temp)
                
        check(root,temp)
        
        
        
        s=set(temp)    #remove duplicate
        
        
        l1=list(s)
        l1.sort()
        
        if len(l1)==1:
            return -1
        else:
            return l1[len(l1)-k]
        
