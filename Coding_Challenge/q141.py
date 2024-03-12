'''
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
'''

class Solution:
    def NumberOFTurns(self, root, first, second):
        res = ''
        def lca(r,p,q):
            if not r:
                return
            if r.data==q or r.data==p:
                return r
            left = lca(r.left,p,q)
            right  = lca(r.right,p,q)
            if left is None:
                return right
            if right is None:
                return left
            return r
        x = lca(root,first,second)
        
        def height(r,t,s):
            nonlocal res
            if not r:
                return False
           
            if r.data==t:
                res = s
                return res
            if r.left:
                height(r.left,t,s+'L')
            if r.right:
                height(r.right,t,s+'R')
        
        a = height(x,first,'')
        a = res
        res = ''
        height(x,second,'')
        b = res
        a1,b1 = 0,0
        for i in range(1,len(a)):
            if a[i]!=a[i-1]:
                a1+=1
        for i in range(1,len(b)):
            if b[i]!=b[i-1]:
                b1+=1
        
        if x.data==first:
            return b1
        elif x.data==second:
            return a1
        return a1+b1+1
