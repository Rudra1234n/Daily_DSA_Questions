"""
# Node Class

class node:
    def __init__(self, val):
        self.data = val
        self.next = None

"""

class Solution:
    #Function to reverse a linked list.
    def reverseList(self, head):
        curr = head
        prev_node = None
        while curr!=None:
            next_node = curr.next
            curr.next = prev_node
            prev_node = curr
            curr = next_node
            
        curr = prev_node
        return curr
        