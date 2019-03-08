def insert_bottom(stack,temp):
    if(len(stack)==0):
        stack.append(temp)
    else:
        element=stack.pop()
        insert_bottom(stack,temp)
        stack.append(element)


def reverse(stack):

    if(len(stack)!=0):
        temp=stack.pop()
        reverse(stack)
        insert_bottom(stack,temp)


if __name__=='__main__' :
    stack=[1,2,3,4,5,6]
    reverse(stack)
    print(*stack)

