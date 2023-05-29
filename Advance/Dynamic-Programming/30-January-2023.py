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


# 3 : Best Time to Buy and Sell Stocks III

# Say you have an array, A, for which the ith element is the price of a given stock on day i.

# Design an algorithm to find the maximum profit. You may complete at most 2 transactions.

# Return the maximum possible profit.

# Note: You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

# Input Format:

# The first and the only argument is an integer array, A.
# Output Format:

# Return an integer, representing the maximum possible profit.
# Constraints:

# 1 <= length(A) <= 7e5
# 1 <= A[i] <= 1e7
# Examples:

# Input 1:
#     A = [1, 2, 1, 2]

# Output 1:
#     2

# Explanation 1: 
#     Day 0 : Buy 
#     Day 1 : Sell
#     Day 2 : Buy
#     Day 3 : Sell

# Input 2:
#     A = [7, 2, 4, 8, 7]

# Output 2:
#     6

# Explanation 2:
#     Day 1 : Buy
#     Day 3 : Sell



class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        #Edge case if A is empty.
        if not A:  
            return 0
        # Initialize buy1 and buy2 to negative A[0] as we want to find the maximum value.
        buy1 = buy2 = -A[0]
        # Initialize sell1 and sell2 to 0.
        sell1 = sell2 = 0

        for i in range(1, len(A)):
            # update buy1, sell1
            buy1 = max(buy1, -A[i])
            sell1 = max(sell1, buy1+A[i])
            # update buy2, sell2
            buy2 = max(buy2, sell1-A[i])
            sell2 = max(sell2, buy2+A[i])
        # Return sell2 as it represents the maximum profit we can earn after two transactions.
        return sell2


#  4 : Unique Binary Search Trees II
# Given an integer A, how many structurally unique BST's (binary search trees) exist that can store values 1...A?



# Problem Constraints
# 1 <= A <=18



# Input Format
# First and only argument is the integer A



# Output Format
# Return a single integer, the answer to the problem



# Example Input
# Input 1:

#  1
# Input 2:

#  2


# Example Output
# Output 1:

#  1
# Output 2:

#  2


# Example Explanation
# Explanation 1:

#  Only single node tree is possible.
# Explanation 2:

#  2 trees are possible, one rooted at 1 and other rooted at 2.

class Solution:
    # @param A : integer
    # @return an integer
    def numTrees(self, A):
        dp = [0] * (A + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, A + 1):
            val = 0
            for j in range(i):
                val += dp[j] * dp[i - j - 1]

            dp[i] = val

        return dp[A]
