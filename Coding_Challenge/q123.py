from collections import defaultdict
class Solution:
    def canPair(self, arr, k):
            if (n & 1):
                return False
            freq = defaultdict(lambda: 0)
            for i in range(0, n):
                freq[((arr[i] % k) + k) % k] += 1
            for i in range(0, n):
                rem = ((arr[i] % k) + k) % k
                if (2 * rem == k):
                    if (freq[rem] % 2 != 0):
                        return False
                elif (rem == 0):
                    if (freq[rem] & 1):
                        return False
                elif (freq[rem] != freq[k - rem]):
                     return False
         
            return True
