class Solution:
    def MedianOfArrays(self, array1, array2):
        arr1=array1+array2
        arr1.sort()
        n=len(arr1)
        if n%2==0:
            median=(arr1[n//2-1]+arr1[n//2])/2
            median = int(median) if median.is_integer() else median
        else:
            median=arr1[n//2]
        return median
