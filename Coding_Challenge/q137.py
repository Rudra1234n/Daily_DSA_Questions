class Solution:
    def calcDistanc(self,arr1,arr2):
        index = 0
        l1 = len(arr1)
        l2 = len(arr2)
        while (index<l1 and index<l2 ) and (arr1[index] == arr2[index]):
            index+=1
        index*=2
        return l1+l2-index

    def findDist(self,root,a,b):
        def traverseDFS(level,node):
            if not node:
                return
            traverseArr.append(node.data)
            if node.data==a or node.data==b:
                finalArr.append(traverseArr[:])
                if len(finalArr)==2:
                    return
            traverseDFS(level+1,node.left)
            traverseDFS(level+1,node.right)
            traverseArr.pop()
        traverseArr=[]
        finalArr=[]
        traverseDFS(0,root)
        if len(finalArr)!=2:
            return 0
        return self.calcDistanc(finalArr[0],finalArr[1])

