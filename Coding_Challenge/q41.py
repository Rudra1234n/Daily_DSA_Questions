class Solution:
    def pushZerosToEnd(self,arr, n):
        k=0
        for i in range(len(arr)):
            if arr[i]!=0:
                arr[k],arr[i]=arr[i],arr[k]
                k+=1
        return arr
