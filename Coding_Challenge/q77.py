class Solution:
    def addOne(self,head):
        import sys
        sys.setrecursionlimit(10**6)
        
        dummy = Node(0)
        dummy.next = head
        
        carry = 0
        def walk(n):
            nonlocal carry
            if not n:
                carry += 1
                return
            walk(n.next)
            d = n.data + carry
            n.data = d%10
            carry = d//10
        walk(dummy)
        return dummy if dummy.data > 0 else dummy.next
