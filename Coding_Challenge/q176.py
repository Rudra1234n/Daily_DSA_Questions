class Solution:
    def cutRod(self, price, n):
        matrix = [0] * (n+1)
        
        for i in range(1, n+1):
            for j in range(1, n+1):
                if i <= j:
                    matrix[j] = max(price[i-1] + matrix[j-i], matrix[j])
                    
        return matrix[n]
