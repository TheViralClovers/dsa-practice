# Returns maximum profit with
# two transactions on a given
# list of stock prices price[0..n-1]


def maxProfit(price, n):

	# Create profit array and initialize it as 0
	profit = [0]*n
	print(profit)
	# Get the maximum profit
	# with only one transaction
	# allowed. After this loop,
	# profit[i] contains maximum
	# profit from price[i..n-1]
	# using at most one trans.
	max_price = price[n-1]
	print(max_price)
	for i in range(n-2, 0, -1):
		print(f"price[{i}]:{price[i]} > max_price:{max_price}")
		if price[i] > max_price:
			max_price = price[i]
			print(f"max_price updated: {max_price}")


		# we can get profit[i] by
		# taking maximum of:
		# a) previous maximum,
		# i.e., profit[i+1]
		# b) profit by buying at
		# price[i] and selling at
		# max_price
		# print(f"profit[{i}]:{profit[i]}")
		# print(profit)
		print(f"max_price - price[i]: {max_price - price[i]}")
		profit[i] = max(profit[i+1], max_price - price[i])
		print(f"profit[{i}]:{profit[i]}")
		print(profit)


	# Get the maximum profit
	# with two transactions allowed
	# After this loop, profit[n-1]
	# contains the result
	min_price = price[0]

	print("Going forward now")
	for i in range(1, n):

		# print(profit)
		print(f"{price[i]} < {min_price}")
		if price[i] < min_price:
			min_price = price[i]
			print(min_price)
		# Maximum profit is maximum of:
		# a) previous maximum,
		# i.e., profit[i-1]
		# b) (Buy, Sell) at
		# (min_price, A[i]) and add
		# profit of other trans.
		# stored in profit[i]
		print(f"profit[{i-1}]:{profit[i-1]},profit[{i}]+price[{i}]-min_price: {profit[i]+(price[i]-min_price)}")
		profit[i] = max(profit[i-1], profit[i]+(price[i]-min_price))
		print(profit)

	result = profit[n-1]

	return result


# Driver function
price = [2, 30, 15, 10, 8, 25, 80]
print ("Maximum profit is", maxProfit(price, len(price)))

# This code is contributed by __Devesh Agrawal__

#gfg soln
# from typing import List


# class Solution:
#     def maxProfit(self, n : int, price : List[int]) -> int:
                
#         profit = [0] * n
#         max_sell_price = price[n-1]
        
#         for i in range(n-2,0,-1):
#             if max_sell_price < price[i]:
#                 max_sell_price = price[i]
                
#             profit[i]=max(profit[i+1],max_sell_price-price[i])
        
#         min_buy_price = price[0]
        
#         for i in range(1,n):
#             if min_buy_price>price[i]:
#                 min_buy_price=price[i]
                
#             profit[i]=max(profit[i-1],profit[i]+price[i]-min_buy_price)
            
#         return profit[n-1]

# #{ 
#  # Driver Code Starts
# class IntArray:
#     def __init__(self) -> None:
#         pass
#     def Input(self,n):
#         arr=[int(i) for i in input().strip().split()]#array input
#         return arr
#     def Print(self,arr):
#         for i in arr:
#             print(i,end=" ")
#         print()


# if __name__=="__main__":
#     t = int(input())
#     for _ in range(t):
        
#         n = int(input())
        
        
#         price=IntArray().Input(n)
        
#         obj = Solution()
#         res = obj.maxProfit(n, price)
        
#         print(res)
        

# # } Driver Code Ends