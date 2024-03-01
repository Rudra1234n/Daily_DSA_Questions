class Solution:

    #Function to find all elements in array that appear more than n/k times.

    def countOccurence(self,arr,n,k):

        #Your code here

        d={}

        for num in arr:

            if num not in d:

                d[num]=1

            else:

                d[num]+=1

        di=n/k

        count=0

        for k,v in d.items():

            if v>di:

                count+=1

        return count
