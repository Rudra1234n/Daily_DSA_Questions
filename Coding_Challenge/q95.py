import math

class Solution:
    
    #Function to delete middle element of a stack.
    def deleteMid(self, s, n):
        # code here
        middle = math.floor(n/2) + 1
        saving = []
        for i in range(0,middle-1):
            saving.append(s.pop())
        s.pop()
        while(saving):
            s.append(saving.pop())
