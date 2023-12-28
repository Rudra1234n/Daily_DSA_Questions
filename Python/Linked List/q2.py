def getNthFromLast(head,n):
    #code here
    if head is None:
        return -1
    # Get the length:
    llen = length(head)
    if llen<n:
        return -1
    
    curr = head
    count = 0
    # Skip the first llen - n nodes
    skip = llen-n
  
    while count<skip:
        curr = curr.next
        count+=1
    return curr.data
    
        
def length(head):
    count = 0
    while head:
        head = head.next
        count+=1
    return count
