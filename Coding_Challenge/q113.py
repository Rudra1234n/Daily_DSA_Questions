class Solution:
 
def nthRowOfPascalTriangle(self,n):
    mod=10**9+7
    result=[]
    for i in range(0,n):
        temp=[1]*(i+1)
        for j in range(1,i):
            temp[j]=(result[j-1]+result[j])%mod
        result=temp
    return temp
