def balancedSum(sales):

    n=len(sales)

    sum_=sum(sales)

    cur=sales[0]
    for i in range(1,n):
        if cur==sum