import math
class Solution:
    def nCr(self, n, r):
        # code here
        if(r>n):
            return 0
        elif(r==1):
            return 1