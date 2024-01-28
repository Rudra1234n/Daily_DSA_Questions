class Solution:  
    def FindMaxSum(self,a, n):
        p1=0;p2=0
        for i in range(n-1,-1,-1):
            s1=0
            if i+1<n:
                s1=p2
            s2=p1
            curr = max(s1+a[i],s2)
            p2=p1
            p1=curr
        return curr
