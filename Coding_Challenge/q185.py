class Solution:
    
    #Function to find if there is a celebrity in the party or not.
    def celebrity(self, M, n):
        # code here 
        ans=-1
        for i in range(n):
            ct1=0
            ct2=0
            for j in range(n):
                if i==j:
                    continue
                if M[i][j]==1:
                    ct1+=1
                if M[j][i]==1:
                    ct2+=1
            if ct1==0 and ct2==n-1:
                ans=i
        return ans
