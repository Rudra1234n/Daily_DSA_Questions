class Solution:
    def find_permutation(self, S):
        if len(S) == 1:
            return [S[0]]
        nextList = []
        for i in range(0,len(S)):
            lstStr = [e for e in S]
            lstStr.pop(i)
            lstStr = ''.join(lstStr)
            fstChr = S[i]
            perm =self.find_permutation(lstStr)
        
            for j in perm:
                if fstChr+j not in nextList:
                    nextList.append(fstChr+j)
        return nextList
