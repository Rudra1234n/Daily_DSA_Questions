class Solution:
    def longestUniqueSubsttr(self, S):
        # code here
        charSet = set()
        l, r, res = 0, 0, 0
        
        for r in range(len(S)):
            while charSet and S[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(S[r])
            res = max(res, r-l+1)
        
        return res
