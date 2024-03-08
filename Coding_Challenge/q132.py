class Solution:
    def wordBreak(self,n, s, dictionary):
        if s == "":
            return 1

        for word in dictionary:
            if s.startswith(word):
                if self.wordBreak(len(s[len(word):]),s[len(word):], dictionary):
                    return 1

        return 0
