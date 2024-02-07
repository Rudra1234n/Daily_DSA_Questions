def Push(x,stack1,stack2):
    '''
    x: value to push
    stack1: list
    stack2: list
    
    '''
    stack1.append(x)
    stack2.append(x)

    #code here

#Function to pop an element from queue by using 2 stacks.
def Pop(stack1,stack2):
    if stack1 == []:
        return - 1
    else:
        return stack1.pop(0)
    if stack2 == []:
        return -1
    else:
        return stack2.pop(0)
    
