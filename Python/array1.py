#User function Template for python3

#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self,arr, n, s): 
       #Write your code here
        ans = []
        j = 0
        total_sum = 0

        for i in range(n):
            total_sum += arr[i]

            while total_sum > s and j <= i:
                total_sum -= arr[j]
                j += 1

            if total_sum == s and  i >= j:
                ans.append(j + 1)
                ans.append(i + 1)
                return ans

        ans.append(-1)
        return ans
