class solution:
  def maximumSumSubarray (self,K,Arr,N):
        ans,max1=0,0
        ans=sum(Arr[:K]) 
        max1=ans
        for j in range(K,N):
            ans+=Arr[j]-Arr[j-K]
            max1=max(max1,ans)
        return max1
