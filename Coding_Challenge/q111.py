def posOfRightMostDiffBit(self,m,n):
        #Your code here
        v=m^n
        res=0
        while v:
            res+=1
            if v%2!=0:
                return res
            v=v//2
        return -1
