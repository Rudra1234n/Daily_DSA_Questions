class Solution:
    def kthSmallest(self,arr, l, r, k):
        new_arr=[]
        for i in arr:
            new_arr.append(i)
        new_arr.sort(reverse=True)
        n=k*-1
        return new_arr[n] 
