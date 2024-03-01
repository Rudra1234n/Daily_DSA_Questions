
class Solution:
    def countZeroes(self, arr, n):
        c = 0
        # arr.sort()
        beg =  0
        end = n-1
        while beg <= end:
            mid = (beg + end) // 2
            if arr[mid] == 0:
                end = mid - 1
            else:
                beg = mid + 1
        return n-1-end 
   
