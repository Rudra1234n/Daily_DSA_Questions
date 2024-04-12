class Solution:
 
def maxIndexDiff(self,arr,n):
maxDiff = 0
        left_min = [float('inf')] * n
        right_max = [float('-inf')] * n
 
        left_min[0] = arr[0]
        for i in range(1, n):
            left_min[i] = min(left_min[i - 1], arr[i])
 
        right_max[n - 1] = arr[n - 1]
        for j in range(n - 2, -1, -1):
            right_max[j] = max(right_max[j + 1], arr[j])
 
        i, j = 0, 0
        while i < n and j < n:
            if left_min[i] <= right_max[j]:
                maxDiff = max(maxDiff, j - i)
                j += 1
            else:
                i += 1
 
        return maxDiff
 
