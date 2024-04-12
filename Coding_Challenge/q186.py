from collections import defaultdict,deque
class Solution:
    def bottomView(self, root):
        D=defaultdict(list)
        Q=deque([(root,0)])
        #Store vertical strips for each width
        while Q:
            i,j=Q.popleft()
            D[j].append((i.data))
            if i.left:
                Q.append((i.left,j-1))
            if i.right:
                Q.append((i.right,j+1))
        #Sort according to width
        k=sorted(D)
        B=[]
        for i in k:
            #Take vertically last element of each strip
            B.append(D[i][-1])#For top view just change to D[i][0]
        return B
