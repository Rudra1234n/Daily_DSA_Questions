from queue import Queue
class Solution:
	def floodFill(self, image, sr, sc, newColor):
	    def dfs (row, col, img, newColor,ans, ini_col, delr,delc):
	        ans[row][col]=newColor
	        q= Queue()
	        l=[row,col]
	        q.put(l)
	        n = len(img)
	        m= len(img[0])
	        while not q.empty():
	            l=q.get()
	            row=l[0]
	            col=l[1]
    	        for i in range(4):
    	            nrow = row+delr[i]
    	            ncol = col +delc[i]
    	            if (nrow>= 0 and nrow< n and ncol>=0 and ncol<m and img[nrow][ncol]==ini_col and ans[nrow][ncol]!= newColor):
    	                ls=[]
    	                ls.append(nrow)
    	                ls.append(ncol)
    	                q.put(ls)
    	                ans[nrow][ncol]= newColor
	    
	    ans = [row[:] for row in image]
	    ini_col = image[sr][sc]
	    delr= [-1,0,1,0]
	    delc = [0,1,0,-1]
	    dfs(sr,sc,image,newColor,ans,ini_col,delr,delc)
	    return ans
