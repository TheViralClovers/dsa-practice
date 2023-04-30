class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit=0
        buy_price=prices[0]
        sell_price=buy_price

        for curr_price in prices[1:]:
            if curr_price<buy_price:
                buy_price = curr_price
                sell_price=buy_price

            if curr_price>sell_price:
                sell_price=curr_price
                profit = sell_price - buy_price
                if profit>max_profit:
                    max_profit = profit

        return max_profit