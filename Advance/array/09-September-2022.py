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


# 4 : Max Non Negative SubArray
# Given an array of integers, A of length N, find out the maximum sum sub-array of non negative numbers from A.

# The sub-array should be contiguous i.e., a sub-array created by choosing the second and fourth element and skipping the third element is invalid.

# Maximum sub-array is defined in terms of the sum of the elements in the sub-array.

# Find and return the required subarray.

# NOTE:

#     1. If there is a tie, then compare with segment's length and return segment which has maximum length.
#     2. If there is still a tie, then return the segment with minimum starting index.

# Examples:

# Input 1:
#     A = [1, 2, 5, -7, 2, 3]

# Output 1:
#     [1, 2, 5]

# Explanation 1:
#     The two sub-arrays are [1, 2, 5] [2, 3].
#     The answer is [1, 2, 5] as its sum is larger than [2, 3].

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):

        n = len(A)
        currentMaxSum = 0
        maxSumSoFar = 0
        startIndex = 0 
        endIndex = 0
        indexTracker = 0
        subArrayLength = 0
        result = []

        for i in range(n):
            if A[i] < 0:
                indexTracker = i+1 # Move start index by one pointer as negative value has encountered 
                currentMaxSum = 0
            else:
                currentMaxSum += A[i]
            
                if currentMaxSum > maxSumSoFar:
                    maxSumSoFar = currentMaxSum
                    startIndex = indexTracker
                    endIndex = i + 1
                    subArrayLength = endIndex - endIndex
                elif currentMaxSum == maxSumSoFar and ((i - indexTracker) > subArrayLength):
                    startIndex = indexTracker
                    endIndex = i+1

        for i in range(startIndex, endIndex):
            result.append(A[i])

        return result


# 5 : Flip
# You are given a binary string A(i.e., with characters 0 and 1) consisting of characters A1, A2, ..., AN. In a single operation, you can choose two indices, L and R, such that 1 ≤ L ≤ R ≤ N and flip the characters AL, AL+1, ..., AR. By flipping, we mean changing character 0 to 1 and vice-versa.

# Your aim is to perform ATMOST one operation such that in the final string number of 1s is maximized.

# If you don't want to perform the operation, return an empty array. Else, return an array consisting of two elements denoting L and R. If there are multiple solutions, return the lexicographically smallest pair of L and R.

# NOTE: Pair (a, b) is lexicographically smaller than pair (c, d) if a < c or, if a == c and b < d.

# Input 1: A = "010"

# Output 1: [1, 1]

# Explanation 1:

# A = "010"

# Pair of [L, R] | Final string
# _______________|_____________
# [1 1]          | "110"
# [1 2]          | "100"
# [1 3]          | "101"
# [2 2]          | "000"
# [2 3]          | "001"

# We see that two pairs [1, 1] and [1, 3] give same number of 1s in final string. So, we return [1, 1].

class Solution:
    # @param A : string
    # @return a list of integers
    def flip(self, A):
        n = len(A)
        newA = []
        currentSum, maxSum, idx = 0, 0, 0
        startIndex, endIndex = -1, -1 
        
        # creating new array from existing array A, if A[i] is 1 add - 1 & if A[i] is 0 add 1 to new array
        for i in range(n):
            x = -1 if A[i] == '1' else 1
            newA.append(x)

        # using kadane's algorithm
        for i in range(n):
            if ((currentSum + newA[i]) < 0):
                currentSum = 0
                idx = i+1
            else:
                currentSum += newA[i]

            if currentSum > maxSum:
                maxSum = currentSum
                startIndex = idx 
                endIndex = i 

        if startIndex == -1:
            return []

        return [startIndex+1,endIndex+1]


# 6 : Rain Water Trapped

# Given a vector A of non-negative integers representing an elevation map where the width of each bar is 1, 
# compute how much water it is able to trap after raining.

# Input 1:
# A = [0, 1, 0, 2]

# Output 1:
# 1

# Explanation 1:

# 1 unit is trapped on top of the 3rd element.

class Solution:
    def trap(self, A):
        n = len(A)

        prefixSumMax = self.getPrefixSumMax(A, n)
        suffixSumMax = self.getSuffixSumMax(A, n)
        result = 0

        for i in range(1, n-1):
            leftMax = prefixSumMax[i-1]
            rightmax = suffixSumMax[i+1]
            level = min(leftMax, rightmax)
            water = level - A[i]

            if water > 0: result += water

        return result


    def getPrefixSumMax(self, A, n):
        prefixSumMax = [0]*n
        prefixSumMax[0] = A[0]

        for i in range(1, n):
            prefixSumMax[i] =  A[i] if A[i] > prefixSumMax[i-1] else prefixSumMax[i-1]

        return prefixSumMax

    def getSuffixSumMax(self, A, n):

        suffixSumMax = [0]*n
        suffixSumMax[n-1] = A[n-1]

        for i in range(n-2, -1, -1):
            suffixSumMax[i]  = A[i] if A[i] > suffixSumMax[i+1] else suffixSumMax[i+1]
        
        return suffixSumMax


