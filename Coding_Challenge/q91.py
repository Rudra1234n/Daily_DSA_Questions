
class Solution:
    #Complete this function
    # Function to find the maximum index difference.
    def maxIndexDiff(self,A, N):
        left=[0]*N
        right=[0]*N
        left[0]=A[0]
        right[N-1]=A[N-1]
        for i in range(1,N):
            left[i]=min(A[i],left[i-1])
        for i in range(N-2,-1,-1):
            right[i]=max(A[i],right[i+1])
            
        i=0
        j=0
        ans=-1
        
        while i<N and j<N:
            if(left[i]<=right[j]):
                ans=max(ans,j-i)
                j+=1
            else:
                i+=1
        return ans
