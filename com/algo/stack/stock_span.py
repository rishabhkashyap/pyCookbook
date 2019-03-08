



def calculate_span(stock_price):
    stack=list()
    span=list()
    span.append(1)
    stack.append(0)
    for i in range(1,len(stock_price)):
        while(len(stack)!=0 and stock_price[stack[-1]]<stock_price[i]):
            stack.pop();
        if(len(stack)==0):
            #in case all previous values are smaller than current value
            span.append(i+1)
        else:
            span.append(i-stack[-1])
        stack.append(i)

    print("Stock span for stock prices \n")
    print(*span)




if __name__=='__main__':
    stock_price=[100, 80, 60, 70, 60, 75, 85]
    calculate_span(stock_price)