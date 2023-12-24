class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def isAnagram(self,a,b):
        acount={}
        bcount={}
        for char in a:
            acount[char]=acount.get(char,0)+1
        for char in b:
            bcount[char]=bcount.get(char,0)+1
        if acount==bcount:
            return True
        else:
            return False
