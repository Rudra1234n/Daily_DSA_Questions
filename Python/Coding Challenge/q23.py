from queue import Queue
class Solution:
    def wordLadderLength(self, startWord, targetWord, wordList):
        #Code here
        n = len(wordList)
        wordLen = len(startWord)
        
        adj = {}
        visited ={}
        #created adj and visited (both are python dictionaries)
        for word in wordList:
            adj[word] = []
            visited[word] = False
        
        # Initialize adj dictionary 
        # Condition: there should be only one char diffrent in connected nodes/words
        for word in wordList:
            for ind in range(len(wordList)):
                currWord = wordList[ind]
                matchCount =0
                for i in range(wordLen):
                    if word[i] == currWord[i]:
                        matchCount+=1
                if matchCount == wordLen-1:
                    l = adj[word]
                    l.append(currWord)
                    adj[word] = l
                    
        q = Queue()       
        # if in: checking if startWord exists in wordList, to initialize Queue of
        if startWord in wordList:
            visited[startWord] =True
            q.put([startWord,1])
        # in else part: adding all words in Queue having exactly one letter different that startWord
        else:
            for ind in range(len(wordList)):
                currWord = wordList[ind]
                matchCount =0
                for i in range(wordLen):
                    if startWord[i] == currWord[i]:
                        matchCount+=1
                if matchCount == wordLen-1:
                    visited[currWord] =True
                    q.put([currWord,2])

        
        #now simple BFS
        while(not q.empty()):
            item = q.get()
            word = item[0]
            noOfTransformation = item[1]

            if word == targetWord:
                return noOfTransformation
            
            for currWord in adj[word]:
                if not visited[currWord]:
                    visited[currWord] = True
                    q.put([currWord,noOfTransformation+1])
              
        return 0          
