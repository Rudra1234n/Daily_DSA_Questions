class Solution:
    def stockBuyAndSell(self, n : int, prices : List[int]) -> int:
        # code here
        
        A = prices
        holding_stock = False
	    stock_bought_price = -1
	    profit = 0
	    
	    i = 0
	    
	    while (i<len(A)):
	        
	        if(i == len(A)-1):
	            if(holding_stock == True):
	                profit += A[i] - stock_bought_price
	        elif(A[i+1] > A[i] and holding_stock == False):
	            holding_stock = True
	            stock_bought_price = A[i]
	        elif(A[i+1] < A[i] and holding_stock == True):
	            holding_stock = False
	            profit += A[i] - stock_bought_price
	            
	        i+=1
	   
	    return profit
