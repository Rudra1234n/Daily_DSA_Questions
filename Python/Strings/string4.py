
class Solution:
    
    #Function to reverse words in a given string.
    def reverseWords(self,S):
        s1=S.split(".")
        s1.reverse()
        
                
        return ".".join(s1)
