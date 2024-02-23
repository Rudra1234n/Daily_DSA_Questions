class Solution:

    def longestSubstrDistinctChars(self, a):
        # code here
        
        res = ''

        for i in range(len(a)):
            temp = ''
            for j in range(i,len(a)):
                if a[j] not in temp:
                    temp += a[j]
                else:
                    break
            if len(temp) > len(res):
                res = temp
        return len(res)
