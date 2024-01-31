class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def rotate(self, head, k):
        current = head
        for i in range(1,k,1):
            current = current.next
            if current.next == None:
                return head
        new_head = current.next
        current.next = None
        current = new_head
        while current.next: 
            current = current.next
        current.next = head
        return new_head
