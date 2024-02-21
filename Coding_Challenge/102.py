class Solution:
    def pairWiseSwap(self, head):
        if not head or not head.next:
            return head
        
        temp = head
        
        while temp and temp.next:
            if temp.data != temp.next.data:
                temp.data, temp.next.data = temp.next.data, temp.data
                
            temp = temp.next.next
        while head:
            print(head.data,end= " ")
            head = head.next
