'''

class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
'''

def flatten(root):
    curr = root
    st = []
    while curr != None:
        temp = curr
        while temp != None:
            st.append(temp.data)
            temp = temp.bottom
        curr = curr.next    
        
    st.sort()
    head_node = Node(0)
    head = head_node
    
    for i in range(len(st)):
        head.bottom = Node(st[i])
        head = head.bottom
        
    return head_node.bottom
