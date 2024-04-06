class Solution:
    def largestPrimeFactor (self, n):
        if n <= 1:
            return n 
        
        largest_prime = -1
        
        while n % 2 == 0:
            largest_prime = 2
            n //= 2
        
        for i in range(3, int(n**0.5) + 1, 2):
            while n % i == 0:
                largest_prime = i
                n //= i
        
        if n > 2:
            largest_prime = n
        
        return largest_prime
