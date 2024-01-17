class Solution:
def pushZerosToEnd(self,arr, n):
    count = 0
    #traverse the array if element is encoutered or not
    for i in range(n):
        if arr[i] != 0:
            #here count is increased
            arr[count]  = arr[i]
            count += 1
            
    while count < n:
        arr[count] = 0
        count += 1 
