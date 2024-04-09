class Solution:
    # Knuth Morris Pratt Algorithm 
	def lps(self, s):
		i = 0
		j = 1
		# STEP 1 - Create lps(longest prefix suffix) array
		lps = [0] * len(s)
		# STEP 2 - Fill the lps array
		# lps[i] will tell us the longest prefix and suffix subarr we can get 
		# in the string till index i
		while j < len(s):
		    if s[i] == s[j]:
		        lps[j] = i + 1
		        i += 1
		        j += 1
		    elif s[i] != s[j]:
		        if i == 0:
		            j += 1
		        elif i != 0:
		            i = lps[i-1]
  		# print(lps)
        # lps[-1] will be your ans
	    return lps[-1]
