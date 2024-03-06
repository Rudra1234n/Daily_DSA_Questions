class Solution:
    def findCatalan(self, n : int) -> int:
        l=[1,1]
        j=0
        while(j!=n-1):
            sum=0
            k=0
            while(k<(len(l))):
                sum+=l[k]*l[-k-1]
                k+=1
            l.append(sum%(1000000007))
            j+=1
        return l[n]
