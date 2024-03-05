#User function Template for python3

from bisect import bisect_right
class Solution:
    def maximumToys(self,N,A,Q,Queries):
        arr = [(A[i],i) for i in range(N)]
        arr.sort()
        new = [0]*N # for storing the indices of all element of array A
        for i in range(N):
            new[arr[i][1]] = i
        
        sort_arr = []
        s = 0
        res = []
        for i in range(N):
            s+=arr[i][0]
            sort_arr.append(s)  # store presum in sorted order
        
        for q in Queries:
            c,n = q[0],q[1]
            idx = bisect_right(sort_arr,c) 
            ans = idx
            if idx>0:
                c-=sort_arr[idx-1]
            else:
                res.append(0)
                continue
    
            broken = set(q[2:])
            # remove all broken toy we choosed.
            for e in broken:
                if new[e-1]<idx:
                    ans-=1
                    c+=A[e-1]
            i = idx 
            # after that we can take at most no. of removed broken toy in prevoius for loop  
            while i<N:
                if c-arr[i][0]>=0:
                    if arr[i][1]+1 not in broken:  #next toy should be not broken
                        c-=arr[i][0]
                        ans+=1
                    i+=1
                else:
                    break
            res.append(ans)
        return res  
