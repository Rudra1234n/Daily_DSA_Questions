class Solution:
    def nextLargerElement(self,arr,n):
        
        ans=[-1]*n
        st=[]
        for i,num in enumerate(arr):
            while st and arr[st[-1]]<num:
                ans[st.pop()]=num
            st.append(i)
        return ans