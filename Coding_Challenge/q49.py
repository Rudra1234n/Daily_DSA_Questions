Class Solution:
  def rearrange(self,arr, n):
        # code here
        posArr = []
        negArr = []
        for i in range(n):
            if arr[i]>=0:
                posArr.append(arr[i])
            else:
                negArr.append(arr[i])
        
        i = 0
        j = 0
        k = 0
        n = len(posArr)
        m = len(negArr)
       
        while i<n and j<m:
            if i>j:
                arr[k] = negArr[j]
                j+=1
                k+=1
            else:
                arr[k] = posArr[i]
                i+=1
                k+=1
                
        while i<n:
                arr[k] = posArr[i]
                i+=1
                k+=1
        while j<m:
                arr[k] = negArr[j]
                j+=1
                k+=1
        return arr
        
