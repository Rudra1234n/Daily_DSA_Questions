
class Solution:
    
    #Function to find the maximum number of activities that can
    #be performed by a single person.
    def activitySelection(self,n,start,end):
        new=list(zip(start,end))
        new.sort()
        count=1
        l=new[0][0]
        h=new[0][1]
        for i in new:
            if (i[0]>l and i[1]<h):
                l=i[0]
                h=i[1]
            elif(i[0]>h):
                count+=1
                l=i[0]
                h=i[1]
        return count
        
