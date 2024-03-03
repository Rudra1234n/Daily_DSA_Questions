class Solution:
    def func(self,p):
        if not p:return 1
        if p.right or p.left:
           if p.right and not p.left:
               if p.data!=p.right.data:return 0
           elif p.left and not p.right:
               if p.data!=p.left.data:return 0
           else:
               if p.data!=p.left.data+p.right.data:return 0
        else:return 1
        return self.func(p.left) and self.func(p.right)
        
    def isSumProperty(self, root):
        return self.func(root)
