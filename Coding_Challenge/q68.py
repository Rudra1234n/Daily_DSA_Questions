class Solution:
    def kthElement(self,  arr1, arr2, n, m, k):
        l=0
        h=2**31-1
        import bisect as bs
        while l<=h:
            m=(l+h)//2
            c=bs.bisect(arr1,m)+bs.bisect(arr2,m)
            if c>=k:
                h=m-1
            else:
                l=m+1
        return l
