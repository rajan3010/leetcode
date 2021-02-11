def maxProfit(prices):

    minPrice=float('inf')
    max_profit=0

    for price in prices:

        minPrice=min(price, minPrice)
        max_profit=max(max_profit,price-minPrice)
    return max_profit

prices = [7,1,5,3,6,4]
print(maxProfit(prices))