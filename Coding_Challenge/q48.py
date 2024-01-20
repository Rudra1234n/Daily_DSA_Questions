class Solution:
    #Function to sort a linked list of 0s, 1s and 2s.
    def segregate(self, head):
        #code here
        a=b=c=0
        temp=head
        while temp:
            if temp.data==0:
                a+=1
            elif temp.data==1:
                b+=1
            elif temp.data==2:
                c+=1
            temp=temp.next
        temp=head
        while a>0:
            temp.data=0
            temp=temp.next
            a-=1
        while b>0:
            temp.data=1
            temp=temp.next
            b-=1
        while c>0:
            temp.data=2
            temp=temp.next
            c-=1
        return head
