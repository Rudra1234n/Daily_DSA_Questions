class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        # code here
        platforms = 0
        maxplatforms = 0
        vals = []
        for i in range(n):
            vals.append((arr[i],1))
            vals.append((dep[i],-1))


        vals = sorted(vals, key=lambda x:x[1], reverse=True)
        vals = sorted(vals, key=lambda x:x[0])
        for i in vals:
            #print(i, end = ' ')
            if i[1] == 1:
                platforms += 1
            elif i[1] == -1:
                platforms -= 1
                
            maxplatforms = max(platforms, maxplatforms)
        
        return maxplatforms