class Solution:
    def matSearch(self,mat, N, M, X): 
        start = 0
        end = M-1
        while (start<N and end>=0):
            if mat[start][end]==X:
                return 1   
            elif mat[start][end]>X:
                end -= 1
            elif mat[start][end]<X:
                start += 1
        return 0 
