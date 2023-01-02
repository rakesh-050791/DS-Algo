# 2 : Maximum array sum after B negations

# Given an array of integers A and an integer B. You must modify the array exactly B number of times. In a single modification, we can replace any one array element A[i] by -A[i].

# You need to perform these modifications in such a way that after exactly B modifications, sum of the array must be maximum.



# Problem Constraints
# 1 <= length of the array <= 5*105
# 1 <= B <= 5 * 106
# -100 <= A[i] <= 100



# Input Format
# The first argument given is an integer array A.
# The second argument given is an integer B.



# Output Format
# Return an integer denoting the maximum array sum after B modifications.



# Example Input
# Input 1:
#  A = [24, -68, -29, -9, 84]
#  B = 4
# Input 2:

#  A = [57, 3, -14, -87, 42, 38, 31, -7, -28, -61]
#  B = 10


# Example Output
# Output 1: 196
# Output 2: 362


# Example Explanation
# Explanation 1:

#  Final array after B modifications = [24, 68, 29, -9, 84]
# Explanation 2:

#  Final array after B modifications = [57, -3, 14, 87, 42, 38, 31, 7, 28, 61]

import heapq as hq
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        hq.heapify(A) 
        
        while B != 0:
            value = hq.heappop(A)
            hq.heappush(A, -value)
            B -= 1
            
        return sum(A)


# 3 : Magician and Chocolates
# Given N bags, each bag contains Bi chocolates. There is a kid and a magician.
# In a unit of time, the kid can choose any bag i, and eat Bi chocolates from it, then the magician will fill the ith bag with floor(Bi/2) chocolates.

# Find the maximum number of chocolates that the kid can eat in A units of time.

# NOTE:

# floor() function returns the largest integer less than or equal to a given number.
# Return your answer modulo 109+7


# Problem Constraints
# 1 <= N <= 100000
# 0 <= B[i] <= INT_MAX
# 0 <= A <= 105



# Input Format
# The first argument is an integer A.
# The second argument is an integer array B of size N.



# Output Format
# Return an integer denoting the maximum number of chocolates the kid can eat in A units of time.



# Example Input
# Input 1:

#  A = 3
#  B = [6, 5]
# Input 2:

#  A = 5
#  b = [2, 4, 6, 8, 10]


# Example Output
# Output 1:

#  14
# Output 2:

#  33


# Example Explanation
# Explanation 1:

#  At t = 1 kid eats 6 chocolates from bag 0, and the bag gets filled by 3 chocolates. 
#  At t = 2 kid eats 5 chocolates from bag 1, and the bag gets filled by 2 chocolates. 
#  At t = 3 kid eats 3 chocolates from bag 0, and the bag gets filled by 1 chocolate. 
#  so, total number of chocolates eaten are 6 + 5 + 3 = 14
# Explanation 2:

#  Maximum number of chocolates that can be eaten is 33.

import heapq
class Solution:
    def nchoc(self, A, B):
        maxheap = []
        for x in B :
            heapq.heappush(maxheap, -x)
        ans = 0
        while A :
            x = heapq.heappop(maxheap)
            ans = ans - x
            heapq.heappush(maxheap, -(-x // 2))
            A -= 1
        return ans % 1000000007
