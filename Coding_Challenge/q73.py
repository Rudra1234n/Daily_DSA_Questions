def length_loop(slow,fast):
    fast=slow.next
    cnt=0
    while fast!=slow:
        cnt+=1
        fast=fast.next
    return cnt+1

def countNodesinLoop(head):
    #Your code here
    if head is None or head.next is None:
        return 0
    fast=head
    slow=head
    while fast is not None and fast.next is not None:
        fast=fast.next.next
        slow=slow.next
        if fast==slow:
            return length_loop(slow,fast)
    return 0

