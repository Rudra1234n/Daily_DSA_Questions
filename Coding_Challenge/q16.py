class Solution:
    def commonElements (self,A, B, C, n1, n2, n3):
        # your code here
        n1=set(A)
        n2=set(B)
        n3=set(C)
        common_ele=n1.intersection(n2,n3)
        return list(sorted(common_ele))