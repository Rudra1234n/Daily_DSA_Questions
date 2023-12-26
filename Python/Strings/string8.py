class Solution:
    def longestCommonPrefix(self, arr, n):
        # code here
        arr.sort()
        wo =''
        x= len(arr[0]) if len(arr[0])<len(arr[-1]) else len(arr[-1])
        for i in range(x):
            if arr[0][i] == arr[-1][i]:
                wo = wo+arr[0][i]
            else:
                break
        if not wo:
            return -1
        return wo
