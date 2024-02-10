class Solution:
    def wordBreak(self, n, dict, s):
        s=s+' '
        m=len(s)
        ans=[]
        def dfs(cur=m-2,prv=m-1,poss=''):
            nonlocal mn,s,dict
            if cur<0:
                if cur==-1 and prv==0:
                    ans.append(poss.strip())
                return
            if s[cur:prv] in dict:
                nposs=s[cur:prv]+' '+poss
                dfs(cur-1,cur,nposs)
            dfs(cur-1,prv,poss)
        dfs()
        return ans
