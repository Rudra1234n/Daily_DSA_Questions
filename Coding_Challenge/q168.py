class Solution:
    def findMaxSum(self,arr, n):
        if n == 1:
            return arr[0]
        if n == 2:
            return max(arr)
        v1 = arr[0]
        v2 = max(arr[0], arr[1])
        max_val = 0
        for i in range(2, n):
            max_val = max(v1 + arr[i], v2)
            v1 = v2
            v2 = max_val
        return max_val
