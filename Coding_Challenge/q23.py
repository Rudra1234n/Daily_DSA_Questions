class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self,A,D,N):
        #Your code here
        d=D
        D=d%N
        A[0:D]=reversed(A[0:D])
        A[D:len(A)]=reversed(A[D:len(A)])
        A[0:len(A)]=reversed(A[0:len(A)])
        return A
