
class Solution:
    #Function to check if a string can be obtained by rotating
    #another string by exactly 2 places.
    def isRotated(self,str1,str2):
        
        if(len(str1) != len(str2)):
            return False
        
        if str2==str1[-2:] + str1[0:-2] or str2==str1[2:] + str1[0:2]:
            return True
        
        return False
        #code here
