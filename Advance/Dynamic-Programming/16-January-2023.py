# 1 : Fibonacci Number

# Given a positive integer A, write a program to find the Ath Fibonacci number.

# In a Fibonacci series, each term is the sum of the previous two terms and the first two terms of the series are 0 and 1. i.e. f(0) = 0 and f(1) = 1. Hence, f(2) = 1, f(3) = 2, f(4) = 3 and so on.

# NOTE: 0th term is 0. 1th term is 1 and so on.



# Problem Constraints
# 0 <= A <= 44



# Input Format
# First and only argument is an integer A.



# Output Format
# Return an integer denoting the Ath Fibonacci number.

# Example Input
# Input 1:

#  A = 4
# Input 2:

#  A = 6


# Example Output
# Output 1:

#  3
# Output 2:

#  8


# Example Explanation
# Explanation 1:

#  Terms of Fibonacci series are: 0, 1, 1, 2, 3, 5, 8, 13, 21 and so on.
#  0th term is 0 So, 4th term of Fibonacci series is 3. 
# Explanation 2:

#  6th term of Fibonacci series is 8.

def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    i = int(input())
    a =0
    b =1
    result = [0,1]
    for x in range(i):
        c = a+b
        result.append(c)
        a = b
        b = c
    print(result[i])
    
    return 0

if __name__ == '__main__':
    main()


# 2 : Minimum Number of Squares
# Given an integer A. Return minimum count of numbers, sum of whose squares is equal to A.

# Problem Constraints
# 1 <= A <= 105


# Input Format
# First and only argument is an integer A.

# Output Format
# Return an integer denoting the minimum count.


# Example Input
# Input 1:

#  A = 6
# Input 2:

#  A = 5


# Example Output
# Output 1:

#  3
# Output 2:

#  2


# Example Explanation
# Explanation 1:

#  Possible combinations are : (12 + 12 + 12 + 12 + 12 + 12) and (12 + 12 + 22).
#  Minimum count of numbers, sum of whose squares is 6 is 3. 
# Explanation 2:

#  We can represent 5 using only 2 numbers i.e. 12 + 22 = 5


class Solution:
    # @param A : integer
    # @return an integer
    def countMinSquares(self, A):
        dp = [A] * (A+1)
        dp[0] = 0

        for i in range(1, A+1):
            for j in range(1, i+1):
                square = j*j

                if i - square < 0:
                    break
                
                dp[i] = min(dp[i], 1 + dp[i - square])
        
        return dp[A]

# other Approaches 

 Top Down Approach

import sys
sys.setrecursionlimit(10**6)

class Solution:
    def countMinSquares(self, A):
        dp = [-1] * (A+1)
        dp[0], dp[1] = 0, 1
        return self.psquares(A, dp)

    def psquares(self, n, dp):
        if n == 0:
            return 0

        if dp[n] != -1:
            return dp[n]

        ans = n
        x = 1

        while (x * x <= n):
            ans = min(ans, self.psquares(n - x * x, dp) )
            x += 1
        
        dp[n] = 1 + ans

        return dp[n]

    # TC: O(NsqrtN); SC: O(N)

# Bottom Up Approach

class Solution:
    # @param A : integer
    # @return an integer
    def countMinSquares(self, A):
        dp = [A] * (A + 1)
        dp[0], dp[1] = 0, 1

        for i in range(A + 1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], 1 + dp[i - j * j])
                j += 1

        return dp[A]

        # TC: O(NsqrtN); SC: O(N)


# 3 : Stairs

# You are climbing a staircase and it takes A steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Return the number of distinct ways modulo 1000000007



# Problem Constraints
# 1 <= A <= 105



# Input Format
# The first and the only argument contains an integer A, the number of steps.



# Output Format
# Return an integer, representing the number of ways to reach the top.



# Example Input
# Input 1:

#  A = 2
# Input 2:

#  A = 3


# Example Output
# Output 1:

#  2
# Output 2:

#  3


# Example Explanation
# Explanation 1:

#  Distinct ways to reach top: [1, 1], [2].
# Explanation 2:

#  Distinct ways to reach top: [1 1 1], [1 2], [2 1].

import sys
sys.setrecursionlimit(10**6)
MODULO = 1000000007

class Solution:
    # @param A : integer
    # @return an integer
    def climbStairs(self, A):
        dp = [-1] * (A + 1)
        if A >= 1: dp[1] = 1
        if A >= 2: dp[2] = 2
        if A >= 3: dp[3] = 3

        return self.calculateStairs(A, dp)
        

    def calculateStairs(self, n, dp):
        if dp[n] != -1:
            return dp[n]

        
        dp[n] = self.calculateStairs(n-1, dp) + self.calculateStairs(n-2, dp)

        return dp[n] % MODULO


# 4 : Max Sum Without Adjacent Elements

# Given a 2 x N grid of integer, A, choose numbers such that the sum of the numbers is maximum and no two chosen numbers are adjacent horizontally, vertically or diagonally, and return it.

# Note: You can choose more than 2 numbers.

# Problem Constraints

# 1 <= N <= 20000
# 1 <= A[i] <= 2000


# Input Format

# The first and the only argument of input contains a 2d matrix, A.


# Output Format

# Return an integer, representing the maximum possible sum.


# Example Input

# Input 1:

#  A = [   
#         [1]
#         [2]    
#      ]
# Input 2:

#  A = [   
#         [1, 2, 3, 4]
#         [2, 3, 4, 5]    
#      ]


# Example Output

# Output 1:

#  2
# Output 2:

#  8


# Example Explanation

# Explanation 1:

#  We will choose 2.
# Explanation 2:

#  We will choose 3 and 5.


import sys 
sys.setrecursionlimit(10**6)
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def adjacent(self, A):
        rows = len(A)
        cols = len(A[0])
        
        ip   = []
        for i in range(cols):
            ip.append(max(A[0][i],A[1][i]))
            
        dp = [-1] * cols 

        return self.getmeMax(cols-1, dp, ip)

    def getmeMax(self,indx,dp,ip):
        if indx < 0:
            return 0
            
        if dp[indx] != -1:
            return dp[indx]
            
        take_it = ip[indx] + self.getmeMax(indx-2,dp,ip)
        dont_tk = self.getmeMax(indx-1,dp,ip)
        dp[indx] = max(take_it,dont_tk)
        
        return dp[indx]


# 5 :  Let's Party

# In Danceland, one person can party either alone or can pair up with another person.

# Can you find in how many ways they can party if there are A people in Danceland?

# Note: Return your answer modulo 10003, as the answer can be large.



# Problem Constraints

# 1 <= A <= 105



# Input Format

# Given only argument A of type Integer, number of people in Danceland.



# Output Format

# Return an integer denoting the number of ways people of Danceland can party.



# Example Input

# Input 1:

#  A = 3
# Input 2:

#  A = 5


# Example Output

# Output 1:

#  4
# Output 2:

#  26


# Example Explanation

# Explanation 1:

#  Let suppose three people are A, B, and C. There are only 4 ways to party
#  (A, B, C) All party alone
#  (AB, C) A and B party together and C party alone
#  (AC, B) A and C party together and B party alone
#  (BC, A) B and C party together and A
#  here 4 % 10003 = 4, so answer is 4.
 
# Explanation 2:

#  Number of ways they can party are: 26.

# Solution Approach :


# Choices - 
# 1. Dance Alone - Ways(n - 1) 
#     We can add the current element to every outcome of the previous combination.
# 2. Dance with a Partner
#     The current person can pair up with (n - 1) persons and with each, 
#     there can be ways(n - 2) combinations. 

# Top down Approach

import sys
sys.setrecursionlimit(10**6)
modulo = 10003

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        dp = [-1] * (A+1)
        if A >= 1: dp[1] = 1
        if A >= 2: dp[2] = 2

        return self.noOfWaysToParty(A, dp) % modulo

    def noOfWaysToParty(self, n, dp):
        if dp[n] != -1:
            return dp[n]
        
        dp[n] = self.noOfWaysToParty(n-1, dp) + (self.noOfWaysToParty(n-2, dp) * (n-1))
        dp[n] %= modulo
        
        return dp[n]

# TC: O(A); SC: O(A)


# 6 : Dice throw

# Given sum A, number of ways you can get that sum with dice roll[1-6].

# As the number of ways can be large return its modulo by 1e9 + 7.



# Problem Constraints

# 1 <= A <= 10 2


# Input Format

# The first argument is the integer A.


# Output Format

# Return an integer .


# Example Input

# Input 1:  A = 3
# Input 2:  A = 4


# Example Output

# Output 1: 4
# Output 2: 8


# Example Explanation

# Explanation 1:

# The four possible ways to obtain 3 are: [1, 1, 1], [1, 2], [2, 1] and [3].

# Explanation 2:

# The eight possible ways to obrain 8 are: [1, 1, 1, 1], [1, 1, 2], [1, 2, 1], [2, 1, 1], [1, 3], [3, 1], [2, 2], [4].


MODULO = 1000000007

class Solution:
    def solve(self, A):
        dp = [0] * (A+1)
        dp[0] = 1
        return self.waysToGetSum(A, dp)

    def waysToGetSum(self, n, dp):
        for i in range(1, n+1):
            dp[i] = 0

            for j in range(1, 7):
                if (i - j >= 0):
                    dp[i] = dp[i] + dp[i-j]

        return dp[n] % MODULO


# 7 : Maximum Sum Value

# You are given an array A of N integers and three integers B, C, and D.

# You have to find the maximum value of A[i]*B + A[j]*C + A[k]*D, where 1 <= i <= j <= k <= N.



# Problem Constraints

# 1 <= N <= 105

# -10000 <= A[i], B, C, D <= 10000



# Input Format

# First argument is an array A
# Second argument is an integer B
# Third argument is an integer C
# Fourth argument is an integer D



# Output Format

# Return an Integer S, i.e maximum value of (A[i] * B + A[j] * C + A[k] * D), where 1 <= i <= j <= k <= N.



# Example Input

# Input 1:

#  A = [1, 5, -3, 4, -2]
#  B = 2
#  C = 1
#  D = -1
# Input 2:

#  A = [3, 2, 1]
#  B = 1
#  C = -10
#  D = 3


# Example Output

# Output 1:

#  18
# Output 2:

#  -4


# Example Explanation

# Explanation 1:

#  If you choose i = 2, j = 2, and k = 3 then we will get
#  A[2]*B + A[2]*C + A[3]*D = 5*2 + 5*1 + (-3)*(-1) = 10 + 5 + 3 = 18
# Explanation 2:

#  If you choose i = 1, j = 3, and k = 3 then we will get
#  A[1]*B + A[3]*C + A[3]*D = (3*1) + (-10*1) + (3*1) = 3 - 10 + 3 = -4

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @return an integer
    def solve(self, A, B, C, D):
        N = len(A)
       
        # Create a dp array to store the answers of previous states
        dp = [[float("-inf")] * 3 for _ in range(N+1)]
       
        for i in range(1, N+1):
            j = i-1  # j is used to keep track of the previous element
           
            # Compute the maximum value of A[i]*B
            dp[i][0] = max(dp[j][0], A[j]*B)
           
            # Compute the maximum value of A[i]*B + A[j]*C
            dp[i][1] = max(dp[j][1], dp[i][0]+A[j]*C)
           
            # Compute the maximum value of A[i]*B + A[j]*C + A[k]*D
            dp[i][2] = max(dp[j][2], dp[i][1]+A[j]*D)
       
   
        return dp[N][2]

# 8 : Max Product Subarray
# Given an integer array A of size N. Find the contiguous subarray within the given array (containing at least one number) which has the largest product.

# Return an integer corresponding to the maximum product possible.

# NOTE: Answer will fit in 32-bit integer value.



# Problem Constraints
# 1 <= N <= 5 * 105

# -100 <= A[i] <= 100



# Input Format
# First and only argument is an integer array A.



# Output Format
# Return an integer corresponding to the maximum product possible.



# Example Input
# Input 1:

#  A = [4, 2, -5, 1]
# Input 2:

#  A = [-3, 0, -5, 0]


# Example Output
# Output 1:

#  8
# Output 2:

#  0


# Example Explanation
# Explanation 1:

#  We can choose the subarray [4, 2] such that the maximum product is 8.
# Explanation 2:

#  0 will be the maximum product possible.

class Solution:
# @param A : tuple of integers
# @return an integer
    def maxProduct(self, A):
        ans, mn, mx = float("-inf"), 1, 1
        for i in range(len(A)):
            if A[i] < 0:
                mx, mn = mn, mx
            mx = max(A[i], mx*A[i])
            mn = min(A[i], mn*A[i])
            ans = max(ans, mx)
        return ans


