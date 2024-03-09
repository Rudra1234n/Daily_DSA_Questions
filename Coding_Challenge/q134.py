class Solution:
    def minCost(self, costs) -> int:
        #your code goes here
        k=len(costs[0])
        n=len(costs)
        if k>1 and n>1:
            for i in range(1,n):
                for b in range(k):
                    costs[i][b]+=min(costs[i-1][:b]+costs[i-1][b+1:])
        if k==1 and n!= 1:
            return -1
        elif n==1 and k==1:
            return costs[0][0]
        else:
            return min(costs[-1]) 
