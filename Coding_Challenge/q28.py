import bisect
class Solution:
    def longestSubsequence(self,arr,n):
        temp = [arr[0]]
        length = 1
        for i in range(1, n):
            if arr[i] > temp[-1]:
                temp.append(arr[i])
                length += 1
            else:
                ind = bisect.bisect_left(temp, arr[i])
                temp[ind] = arr[i]
        return length  