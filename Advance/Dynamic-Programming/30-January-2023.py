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


# 4 : Matrix Chain Multiplication

# Given an array of integers A representing chain of 2-D matices such that the dimensions of ith matrix is A[i-1] x A[i].

# Find the most efficient way to multiply these matrices together. The problem is not actually to perform the multiplications, but merely to decide in which order to perform the multiplications.

# Return the minimum number of multiplications needed to multiply the chain.



# Problem Constraints
# 1 <= length of the array <= 1000
# 1 <= A[i] <= 100



# Input Format
# The only argument given is the integer array A.



# Output Format
# Return an integer denoting the minimum number of multiplications needed to multiply the chain.



# Example Input
# Input 1:

#  A = [40, 20, 30, 10, 30]
# Input 2:

#  A = [10, 20, 30]


# Example Output
# Output 1:

#  26000
# Output 2:

#  6000


# Example Explanation
# Explanation 1:

#  Dimensions of A1 = 40 x 20
#  Dimensions of A2 = 20 x 30
#  Dimensions of A3 = 30 x 10
#  Dimensions of A4 = 10 x 30
#  First, multiply A2 and A3 ,cost = 20*30*10 = 6000
#  Second, multilpy A1 and (Matrix obtained after multilying A2 and A3) =  40 * 20 * 10 = 8000
#  Third, multiply (Matrix obtained after multiplying A1, A2 and A3) and A4 =  40 * 10 * 30 = 12000
#  Total Cost = 12000 + 8000 + 6000 =26000
# Explanation 2:

#  Cost to multiply two matrices with dimensions 10 x 20 and 20 x 30 = 10 * 20 * 30 = 6000.


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        N=len(A)
        dp=[[None]*N for i in range(N)]  # Initialize table for minimum costs
        
        def MCM(A,i,j):
            if i==j:  # Base case: subchain of length 1 costs 0 to multiply
                return 0
            
            if dp[i][j]:  # Check if minimum cost has already been computed
                return dp[i][j]
            
            min_cost = float('inf')
            for k in range(i,j):
                # Compute cost of multiplying subchains A[i:k+1] and A[k+1:j+1]
                cost = MCM(A,i,k) + MCM(A,k+1,j) + A[i-1]*A[k]*A[j]
                
                if cost < min_cost:  # Update minimum cost and optimal split
                    min_cost = cost
                    dp[i][j] = min_cost
            
            return min_cost  
        
        ans = MCM(A,1,N-1)  # Compute minimum cost of multiplying entire chain
        
        return ans  

