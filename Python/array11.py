class Solution:
    
    
    def ispar(self,x):
        s1=[]
        dict1={')': '(', '}': '{', ']': '['}
        for i in x:
            if i in dict1.values():
                s1.append(i)
            elif i in dict1:
                if not s1 or s1.pop()!=dict1[i]:
                    return False
        return not s1

