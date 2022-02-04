from typing import List

from test_framework import generic_test

# min max
# 


def buy_and_sell_stock_once(prices: List[float]) -> float:
    stock_min = prices[0]
    max_profit = 0
    for price in prices:
        stock_min = min(price, stock_min)
        profit = price - stock_min
        if profit > max_profit:
            max_profit = profit
    return max_profit










    # pmin = prices[0]
    # profit_max = 0
    # for price in prices:
    #     if price < pmin:
    #         pmin = price
    #     if (price-pmin) > profit_max:
    #         profit_max = price-pmin
    # return profit_max
    # # i_min = 0
    # # i_max = 0
    # for i in range(1, len(prices)):

    # p_min = prices[0]
    # p_max = prices[0]
    # profit_max = 0
    # ascending = False
    # p_last = prices[0]
    # for i in range(1, len(prices)):
    #     val = prices[i]
    #     if val > p_last:
    #         ascending = True
    #     if val > 
    #     if val > p_max:
    #         p_max = val


    # TODO - you fill in here.
    return 0.0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
