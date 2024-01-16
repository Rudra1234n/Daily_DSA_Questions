class Solution:
     def floorSqrt(self, x):
        beg = 0
        end = x
        root = 0.0
        p = 3
        while beg <= end:
            mid = (beg + end)//2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                end = mid  - 1
            else:
                beg = mid + 1
        incr = 0.1
        for i in range(p):
            while root * root <= x:
                root += incr
            root -=incr
            incr /=10
        return int(root)
