class Solution:
    def palindromeSubStrs(self, s):
        # O(n2)/O(n)
        n=len(s)
        uni={}
        for i in s:
            if i in uni: uni[i]+=1
            else: uni[i]=1
    
        count=len(uni) # # len(uni) == distinct characters and single character is also a palidrome
        distinct=set()
        start=0
    
        for i in range(1,n):
            # even length palindrome
            l=i-1
            r=i
            while l>=0 and r<n and s[l]==s[r]:
                start = l
                sub=s[start:start+r-l+1]
                if sub not in distinct and len(sub)%2==0:
                    distinct.add(sub)
                    count+=1
    
                l-=1
                r+=1
    
            # odd length palindrome
            l=i-1
            r=i+1
            while l>=0 and r<n and s[l]==s[r]:
                start = l
                sub = s[start:start+r-l+1]
                if sub not in distinct and len(sub)%2==1:
                    distinct.add(sub)
                    count+=1
    
                l-=1
                r+=1
    
        # print(distinct)
        return count
