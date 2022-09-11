# 1 : Max Sum Contiguous Subarray

# Find the contiguous non-empty subarray within an array, A of length N, with the largest sum.
# Example Input
# Input 1:

# A = [1, 2, 3, 4, -10] 

# Example Output
# Output 1:
# 10 

# Example Explanation
# Explanation 1:

#  The subarray [1, 2, 3, 4] has the maximum possible sum of 10.

class Solution:
    def maxSubArray(self, A):
        n = len(A)
        currentSum = 0
        currentMax = float('-inf')

        for i in range(n):
            currentSum += A[i]
            currentMax = max(currentMax, currentSum)
            
            if currentSum < 0: currentSum = 0 
        return currentMax


# What’s the difference between Carryforward and prefix sum ?
# What is Kadan's algorithem ?


# 2 : Beggars Outside Temple 
# There are A beggars sitting in a row outside a temple. Each beggar initially has an empty pot. When the devotees come to the temple, they donate some amount of coins to these beggars. Each devotee gives a fixed amount of coin(according to their faith and ability) to some K beggars sitting next to each other.

# Given the amount P donated by each devotee to the beggars ranging from L to R index, where 1 <= L <= R <= A, find out the final amount of money in each beggar's pot at the end of the day, provided they don't fill their pots by any other means.
# For ith devotee B[i][0] = L, B[i][1] = R, B[i][2] = P, Given by the 2D array B

# Example Input
# Input 1:-
# A = 5
# B = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]

# Example Output
# Output 1:-
# 10 55 45 25 25

# Explanation 1:-
# First devotee donated 10 coins to beggars ranging from 1 to 2. Final amount in each beggars pot after first devotee: [10, 10, 0, 0, 0]
# Second devotee donated 20 coins to beggars ranging from 2 to 3. Final amount in each beggars pot after second devotee: [10, 30, 20, 0, 0]
# Third devotee donated 25 coins to beggars ranging from 2 to 5. Final amount in each beggars pot after third devotee: [10, 55, 45, 25, 25]


class Solution:
    def solve(self, A, B):
        n = len(B)
        A = [0] * A

        for element in range(n):
            i = B[element][0] - 1 # Doing - 1 so that 0 based indexing can be maintained
            j = B[element][1] - 1 # Doing - 1 so that 0 based indexing can be maintained
            x = B[element][2]

            A[i] += x
            if j + 1 < len(A):
                A[j + 1] -= x

        # Calculating prefix of A
        for i in range(1, len(A)):
            A[i] = A[i-1] + A[i]

        return A


# 3 : Add One To Number

# Given a non-negative number represented as an array of digits, add 1 to the number ( increment the number represented by the digits ).

# The digits are stored such that the most significant digit is at the head of the list.

# NOTE: Certain things are intentionally left unclear in this question which you should practice asking the interviewer. For example: for this problem, the following are some good questions to ask :

# Q: Can the input have 0's before the most significant digit. Or, in other words, is 0 1 2 3 a valid input? 
# A: For the purpose of this question, YES
# Q: Can the output have 0's before the most significant digit? Or, in other words, is 0 1 2 4 a valid output?                                                  
# A: For the purpose of this question, NO. Even if the input has zeroes before the most significant digit.

# Example Input
# Input 1:

# [1, 2, 3]

# Example Output
# Output 1:

# [1, 2, 4]

# Explanation 1:

# Given vector is [1, 2, 3].
# The returned vector should be [1, 2, 4] as 123 + 1 = 124.


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):

        intToNums = ''
        result = []

        for i in A:
            intToNums += str(i)

        addOneToNums = str(int(intToNums) + 1)

        for i in addOneToNums:
            result.append(int(i))

        return result

