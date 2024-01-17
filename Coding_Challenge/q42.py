class Solution:
    def deleteNode(self,curr_node):
        while curr_node.next:
            if curr_node.next.next==None: curr_node.next
            curr_node.data=curr_node.next.data
            if curr_node.next.next==None:
                curr_node.next=None
                break
            curr_node=curr_node.next
