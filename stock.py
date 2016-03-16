def get_profit(prices):
    max_profit = 0
    count = 0
    for i in range(len(prices)):
        for j in range(len(prices)):
            start = min(i, j)
            end   = max(i, j)

            start_price = min(prices[i], prices[j])
            end_price   = max(prices[i], prices[j])

            profit = end_price - start_price

            max_profit = max(max_profit, profit)
            count += 1

    print ('Loop:', count)
    return max_profit
def get_profit2(prices):
    max_profit = 0
    count = 0
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            start = min(i, j)
            end   = max(i, j)

            start_price = min(prices[i], prices[j])
            end_price   = max(prices[i], prices[j])

            profit = end_price - start_price

            max_profit = max(max_profit, profit)
            count += 1

    print ('Loop:', count)
    return max_profit
def get_profit3(prices):
    if len(prices) < 2:
        raise IndexError('Not enough information')
    max_profit = prices[1] - prices[0]
    count = 0
    smallest = prices[0]
    for i in range(1, len(prices)):
        max_profit = max(max_profit, prices[i]-smallest)
        smallest = min(smallest, prices[i])
        count+=1

    print ('Loop:', count)
    return max_profit

stock_prices_yesterday = [10, 9]
print('Items in array: ', len(stock_prices_yesterday))
print(get_profit(stock_prices_yesterday))
print(get_profit2(stock_prices_yesterday))
print(get_profit3(stock_prices_yesterday))
