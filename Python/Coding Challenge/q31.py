def firstRepeated(self,arr, n):
        s=10000
        d={}
        for i in range(n):
            if arr[i] not in d:
                d[arr[i]]=i+1
            elif d[arr[i]]<0:
                continue
            else:
                d[arr[i]]*=-10
                
        for i in d:
            if d[i]%-10==0 and d[i]<0:
                s=min(s,d[i]//-10)
        if s==10000:
            return -1
        else:
            return s
