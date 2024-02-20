def printFirstNegativeInteger( A, N, K):
    
    def find_it(arr):
        
        for i in arr:
            if i < 0:
                return i
                break
        return  0 
    i = 0 
    
    res =[]
    k = K
        
    while i < N-k+1:
        ele = find_it(A[i:i+k])
        res.append(ele)
        i+=1
    return res
        
