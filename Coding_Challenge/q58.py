class Solution:	
	def remove_duplicate(self,A,N):
        # code here
        A.append(0.0)
        i=0
        j=1
        while True:
            if N==1:
                return N
            if A[j]==0.0:
                break
            if A[i]!=A[j]:
                i+=1
                j+=1
            if A[i]==A[j]:
                A.pop(j)
        A.remove(0.0)
        return len(A)
