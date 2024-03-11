'''
class Pair(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
'''
class Solution:
    def maxChainLen(self, p, n):
        if n == 0:
            return 0
        
        p.sort(key=lambda x: x.b)  # Assuming 'b' is the second element
        ans = 1
        last = p[0].b
        
        for i in range(1, n):
            if p[i].a > last:
                last = p[i].b
                ans += 1
        
        return ans
