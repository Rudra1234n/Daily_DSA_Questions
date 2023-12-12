def lcs(self,x,y,s1,s2):
        
        # code here
        t = [[-1 for _ in range(y+1)]for _ in range(x+1)]
        for i in range(x):
            for j in range(y):
                if i==0 or j==0:
                    t[i][j] =0
        for i in range(1,x+1):
            for j in range(1,y+1):
                if s1[i-1] == s2[j-1]:
                    t[i][j] = (1+t[i-1][j-1])%1000000001
                else:
                    t[i][j] = max(t[i][j-1],t[i-1][j])%1000000001
        return t[x][y]