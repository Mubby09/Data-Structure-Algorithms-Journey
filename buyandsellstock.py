# def buy_and_sell(prices):
#     current_minimum_price = prices[0]
#     current_max_profit = 0
#     for price in prices:
#         max_profit_today = price - current_minimum_price
#         current_max_profit = max(current_max_profit, max_profit_today)
#         current_minimum_price = min(current_minimum_price, price)
#     return print(current_max_profit)


# buy_and_sell([869.0, 737.0, 633.0, 737.0, 909.0])
# buy_and_sell([310, 315, 275, 295, 260, 270, 290, 230, 255, 250])

def buy_and_sell(prices):
    currentMinimumPrice = float('inf')
    currentMaxProfit = 0

    for price in prices:
        MaxProfitToday = price - currentMinimumPrice
        currentMaxProfit = max(MaxProfitToday, currentMaxProfit)
        currentMinimumPrice = min(currentMinimumPrice, price)

    return print(currentMaxProfit)


buy_and_sell([869.0, 737.0, 633.0, 737.0, 909.0])
buy_and_sell([310, 315, 275, 295, 260, 270, 290, 230, 255, 250])
