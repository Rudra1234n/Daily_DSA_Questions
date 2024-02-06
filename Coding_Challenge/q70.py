def fourSum(self, arr, k):
        arr.sort()
        n = len(arr)
        res = []
        for i in range(n):
            for j in range(i+1, n):
                target = k - arr[i] - arr[j]
                s = j + 1
                e = n - 1
                while s < e:
                    if arr[s] + arr[e] < target:
                        s += 1
                    elif arr[s] + arr[e] > target:
                        e -= 1
                        
                    else:
                        quad = [arr[i], arr[j], arr[s], arr[e]]
                        res.append(quad)
                        
                        while s < e and arr[s] == quad[2]:
                            s += 1  
                        
                        while s < e and arr[e] == quad[3]:
                            e -= 1 
                           
                    while j + 1 < n and arr[j] == arr[j + 1]:
                        j += 1 
                  
                   
            while i + 1 < n and arr[i] == arr[i + 1]:
                i += 1  
              
                
        return res   
