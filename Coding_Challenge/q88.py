class Solution:
    
    #Function to calculate the span of stockâ€™s price for all n days.
    def calculateSpan(self,a,n):
        l=[1]*n
        s=[0]
        for i in range(n):
            while s and a[s[-1]]<=a[i]:
                s.pop()
            l[i]=i-s[-1] if s else i+1
            s.append(i)
        return l
       
