def minimumPlatform(self,n,arr,dep):
        # code here
        platforms = 0
        maxplatforms = 0
        vals = []
        for i in range(n):
            vals.append((arr[i],1))
            vals.append((dep[i],-1))
