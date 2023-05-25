# 1 : Best Time to Buy and Sell Stocks I

# Say you have an array, A, for which the ith element is the price of a given stock on day i.
# If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

# Return the maximum possible profit.



# Problem Constraints
# 0 <= A.size() <= 700000
# 1 <= A[i] <= 107



# Input Format
# The first and the only argument is an array of integers, A.


# Output Format
# Return an integer, representing the maximum possible profit.


# Example Input
# Input 1:
# A = [1, 2]
# Input 2:

# A = [1, 4, 5, 2, 4]


# Example Output
# Output 1:
# 1
# Output 2:

# 4


# Example Explanation
# Explanation 1:
# Buy the stock on day 0, and sell it on day 1.
# Explanation 2:

# Buy the stock on day 0, and sell it on day 2.

class Solution:
	# @param A : tuple of integers
	# @return an integer
	def maxProfit(self, A):
        prices = A 

        maxProfit = 0
        minBuyingPrice = float('inf')

        for currentPrice in prices:
            minBuyingPrice = min(minBuyingPrice, currentPrice)
            currentProfit = currentPrice-minBuyingPrice 
            maxProfit = max(currentProfit, maxProfit)
        return maxProfit

# 2 : Best Time to Buy and Sell Stocks II

# Say you have an array, A, for which the ith element is the price of a given stock on day i.

# Design an algorithm to find the maximum profit.

# You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

# However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).



# Problem Constraints
# 0 <= len(A) <= 1e5
# 1 <= A[i] <= 1e7


# Input Format
# The first and the only argument is an array of integer, A.


# Output Format
# Return an integer, representing the maximum possible profit.


# Example Input
# Input 1:
# A = [1, 2, 3]
# Input 2:
# A = [5, 2, 10]


# Example Output
# Output 1:
# 2
# Output 2:
# 8


# Example Explanation
# Explanation 1:
#     => Buy a stock on day 0.
#     => Sell the stock on day 1. (Profit +1)
#     => Buy a stock on day 1.
#     => Sell the stock on day 2. (Profit +1)

#     Overall profit = 2
# Explanation 2:
#     => Buy a stock on day 1.
#     => Sell the stock on on day 2. (Profit +8)

#     Overall profit = 8


class Solution:
	# @param A : tuple of integers
	# @return an integer
	def maxProfit(self, A):
        n = len(A)
        prices = A 

        profit = 0

        for i in range(1, n):
            if prices[i] > prices[i - 1]:
                profit += (prices[i] -  prices[i - 1])
        
        return profit

