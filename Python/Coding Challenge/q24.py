from string import ascii_lowercase
from collections import deque

class Solution:
	def wordLadderLength(self, startWord, targetWord, wordList):
		
		hash_map = {}
		for i in range(len(wordList)):
		    hash_map[wordList[i]] = 1
		    
		q = deque([])
		q.append((startWord,0))
		
		while q:
		    word , step = q.popleft()
		    if word == targetWord:
		        return step+1
		        
		    for i in range(len(word)):
		        w = word
		        for j in ascii_lowercase:
		            w = w[:i] + j + w[i+1:]
		            if w in hash_map:
		                q.append((w,step+1))
		                del hash_map[w]
        return 0 
