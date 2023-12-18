class Solution:
    def majorityElement(self, A, N):
        #Your code here
        dic = {}
        if len(A) == 1:
            return A[0]
        for i in range(0, len(A)):
            dic[A[i]] = dic.get(A[i], 0)+1
        for i in A:
            if dic[i] > N//2:
                return i
        return -1
