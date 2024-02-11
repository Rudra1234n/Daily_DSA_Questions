def factorial(self,N):
        div=10**9+7
        l=[1 for i in range(N+1)]
        inv=[1 for i in range(N+1)]
        for i in range(2,N+1):
            l[i]=(i*l[i-1])%div
            inv[i]=pow(l[i],div-2,div)
            
        return (l,inv)
        
    def bestNumbers(self, N : int, A : int, B : int, C : int, D : int) -> int:
        # code here
        div=10**9+7
        res=0
        if A==B:
            s=str(N*A)
            if str(C) in s or str(D) in s:
                res=1
        else:
            possible_sums=[]
            for i in range(N+1):
                s=(A*i+B*(N-i))
                s=str(s)
                if str(C) in s or str(D) in s:
                    possible_sums.append((i,N-i))
                    
            fact,inv=self.factorial(N)
            res=0
            for n1,n2 in possible_sums:
                res+=(fact[-1]*inv[n1]*inv[n2])%div
        
        return res%(div)

Passing 1127/1131 before TLE

