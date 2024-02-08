class Solution:
    def maxSumIS(self, Arr, n):
        # code here
        
        def help(arr,i,prev,memo):
            if(i >= len(arr)):
                return 0
            if memo[i][prev] != -1:
                return memo[i][prev]
            s = ns = 0
            if prev != -1 and arr[i] <= arr[prev]:
                ns = help(arr,i+1,prev,memo)
            else:
                s = arr[i] + help(arr,i+1,i,memo)
                ns = help(arr,i+1,prev,memo)
            memo[i][prev] = max(s,ns)
            return max(s,ns)
        
        memo = [[-1 for _ in range(len(Arr))] for _ in range(len(Arr))]
        return help(Arr,0,-1,memo)
