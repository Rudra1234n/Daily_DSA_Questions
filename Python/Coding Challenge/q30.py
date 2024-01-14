class Solution:

    def findMinDiff(self, A,N,M):
        A.sort()
        ans=float('inf')
        for i in range((N-M)+1):
            num=A[i+M-1]-A[i]
            if num<ans:
                ans=num
        return ans
