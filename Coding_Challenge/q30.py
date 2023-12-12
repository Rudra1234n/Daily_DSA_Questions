def find3Numbers(self,A, n, X):
        A.sort()
        for i in range(n):
            remain = X - A[i]
            left,right = i+1,n-1
            while left < right :
                if A[left] + A[right] > remain:
                    right -= 1
                elif A[left] + A[right] < remain:
                    left += 1 
                else :
                    return 1
        return 0