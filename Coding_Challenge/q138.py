class Solution:
    def maxGold(self, n, m, M):
    for j in range(m-1,0,-1):
        for i in range(1,n+1):
            temp=0
            for dx in [-1,0,1]:
                x=i+dx
                if x>0 and x<=n:
                    temp=max(temp,M[x-1][j])
            M[i-1][j-1]+=temp
    res=0
    for i in range(1,n+1):
        res=max(res,M[i-1][0])
    return res
        
