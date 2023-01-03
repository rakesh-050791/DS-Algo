# 1 : Product of 3

# Given an integer array A of size N.

# You have to find the product of the three largest integers in array A from range 1 to i, where i goes from 1 to N.

# Return an array B where B[i] is the product of the largest 3 integers in range 1 to i in array A. If i < 3, then the integer at index i in B should be -1.

# Input Format
# First and only argument is an integer array A.

# Output Format
# Return an integer array B. B[i] denotes the product of the largest 3 integers in range 1 to i in array A.

# Example Input
# Input 1: A = [1, 2, 3, 4, 5]
# Input 2: A = [10, 2, 13, 4]


# Example Output
# Output 1: [-1, -1, 6, 24, 60]
# Output 2: [-1, -1, 260, 520]


# Example Explanation
# Explanation 1:

#  For i = 1, ans = -1
#  For i = 2, ans = -1
#  For i = 3, ans = 1 * 2 * 3 = 6
#  For i = 4, ans = 2 * 3 * 4 = 24
#  For i = 5, ans = 3 * 4 * 5 = 60

#  So, the output is [-1, -1, 6, 24, 60].
 
# Explanation 2:

#  For i = 1, ans = -1
#  For i = 2, ans = -1
#  For i = 3, ans = 10 * 2 * 13 = 260
#  For i = 4, ans = 10 * 13 * 4 = 520

#  So, the output is [-1, -1, 260, 520].


# Approach using heap library 
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):

        pq = []
        ans = []
        for i in range(0, len(A)):

            heapq.heappush(pq, -A[i])
            # Append -1 to the answer as number of elements are < 3.
            if i < 2:
                ans.append(-1)
            else:
                # take 3 maximum elements from queue.
                # Pop will give minimum, as we have added elements after multiplying by minus one.
                x = heapq.heappop(pq)
                y = heapq.heappop(pq)
                z = heapq.heappop(pq)

                val = x * y * z
                # append -val to answer, as we have added elements after multiplying by minus one.
                ans.append(-val)

                # append all these numbers back to queue
                heapq.heappush(pq, x)
                heapq.heappush(pq, y)
                heapq.heappush(pq, z)

        return ans
        
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


# 4 : Connect ropes
# You are given an array A of integers that represent the lengths of ropes.

# You need to connect these ropes into one rope. The cost of joining two ropes equals the sum of their lengths.

# Find and return the minimum cost to connect these ropes into one rope.



# Problem Constraints
# 1 <= length of the array <= 100000
# 1 <= A[i] <= 1000



# Input Format
# The only argument given is the integer array A.



# Output Format
# Return an integer denoting the minimum cost to connect these ropes into one rope.



# Example Input
# Input 1:

#  A = [1, 2, 3, 4, 5]
# Input 2:

#  A = [5, 17, 100, 11]


# Example Output
# Output 1:

#  33
# Output 2:

#  182


# Example Explanation
# Explanation 1:

#  Given array A = [1, 2, 3, 4, 5].
#  Connect the ropes in the following manner:
#  1 + 2 = 3
#  3 + 3 = 6
#  4 + 5 = 9
#  6 + 9 = 15

#  So, total cost  to connect the ropes into one is 3 + 6 + 9 + 15 = 33.
# Explanation 2:

#  Given array A = [5, 17, 100, 11].
#  Connect the ropes in the following manner:
#  5 + 11 = 16
#  16 + 17 = 33
#  33 + 100 = 133

#  So, total cost  to connect the ropes into one is 16 + 33 + 133 = 182.

import heapq
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        sums = 0
        heapq.heapify(A)
        while len(A) > 1:
            x = heapq.heappop(A)
            y = heapq.heappop(A)
            sums = sums + x + y
            heapq.heappush(A, x + y)
        return sums
        