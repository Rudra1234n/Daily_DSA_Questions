class Solution:
    def findMaxLen(ob, S):
        n = len(S)

        stk = [-1]
        result = 0

        for i in range(n):
            if S[i] == '(':
                stk.append(i)
            else:
                if stk:
                    stk.pop()
                    if not stk:
                        stk.append(i)
                    else:
                        result = max(result, i - stk[-1])
                else:
                    stk.append(i)

        return result
