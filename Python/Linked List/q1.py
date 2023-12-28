class Solution:
    #Function to remove a loop in the linked list.
    def removeLoop(self, head):
        v=set()
        while head:
            if head in v or head.next in v:
                head.next=None
            v.add(head)
            head=head.next
        return head# code here
