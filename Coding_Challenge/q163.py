class Solution:
     def countSubarray(self, n, nums, k):  
        def hashim(n,nums,k):
            d={0:1}
            ans=0
            cur=0 
            sum=0
            n=len(nums)
            for i in range(n):
                if nums[i]<k:
                    sum-=1 
                    if sum in d:
                        cur-=d[sum]
                else:
                    if sum in d:
                        cur+=d[sum]
                    sum+=1 
                ans+=cur 
                if sum in d:
                    d[sum]+=1 
                else:
                    d[sum]=1 
            return ans  
                    
        return hashim(n,nums,k)-hashim(n,nums,k+1)
