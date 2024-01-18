class Solution:
    
    #Function to check if two strings are isomorphic.
    def areIsomorphic(self,str1,str2):
        n = len(str1)
        m = len(str2)
        pairs={}
        
        if n!=m:
            return False
        if n==1:
            return True
        for i in range(n):
            if str1[i] not in pairs:
                if str2[i] in pairs.values():
                    return False
                pairs[str1[i]]=str2[i]
            elif pairs[str1[i]]!=str2[i]:
                return False
        return True
