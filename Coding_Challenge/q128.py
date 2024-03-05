'''
#LinkedList Node
class LNode:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        
#Tree Node        
class TNode:
    def __init__(self, data):
        self.data=data
        self.left = self.right = None
'''

class Solution:
    def sortedListToBST(self, head):
        #code here
        arr=[]
        while head:
            arr.append(head.data)
            head=head.next
        
        def make(arr,start,end):
            if start>end:
                return None
            mid=(start+end)//2
            if (start+end+1)%2==0:
                mid+=1
                root=TNode(arr[mid])
                root.left=make(arr,start,mid-1)
                root.right=make(arr,mid+1,end)
            else:
                root=TNode(arr[mid])
                root.left=make(arr,start,mid-1)
                root.right=make(arr,mid+1,end)
            return root
            
        return make(arr,0,len(arr)-1)
