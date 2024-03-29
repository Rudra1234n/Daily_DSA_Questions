from collections import OrderedDict

class Solution:
    def verticalOrder(self, root): 
        odict=OrderedDict()
        queue=[[root,0,0]]
        while queue:
            a=queue.pop(0) 
            node=a[0] 
            vertical=a[1] 
            level=a[2] 
            if vertical not in odict: 
                odict[vertical]=[[level,node.data]]
            else:
                odict[vertical].append([level,node.data])
            if node.left:
                queue.append([node.left,vertical-1,level+1])
            if node.right:
                queue.append([node.right,vertical+1,level+1])
        sorted_dict=sorted(odict.items(),key=lambda x:x[0]) # sort according to vertical
        result=[] 
        for i in sorted_dict:
            for j in i[1]: # takes level-data pairs
                result.append(j[1]) #takes data
        return result
