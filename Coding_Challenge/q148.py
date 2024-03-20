class Solution:
    def __init__(self):
        self.c=1
    def isLucky(self, n): 
        #RETURN True OR False
        self.c+=1
        if(n/self.c == n//self.c ):
            return False
        elif(n/self.c < 1):
            return True
        return self.isLucky(n-n//(self.c))
