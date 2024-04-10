class Solution:
    #Function to add two numbers represented by linked list.
    def addTwoLists(self, num1, num2):
        n = ''
        m = ''
        while num1:
            n = n+str(num1.data) 
            num1 = num1.next
        while num2:
            
            m = m+str(num2.data) 
            num2 = num2.next
        s = str(int(n) + int(m))
        
        head = Node(-1)
        p = head
        for digit in s:
            p.next = Node(int(digit))
            p = p.next
        return head.next
