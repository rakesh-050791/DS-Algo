# 1 : Subarray with given sum

# Given an array of positive integers A and an integer B, find and return first continuous subarray which adds to B.

# If the answer does not exist return an array with a single element "-1".

# First sub-array means the sub-array for which starting index in minimum.

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        n = len(A)

        left, right, currentSum = 0, 0, 0

        while left < n and right < n:

            if currentSum < B:
                currentSum += A[right]
                right += 1

            if currentSum > B:
                currentSum -= A[left]
                left += 1

            if currentSum == B:
                return(A[left:right])
        return [-1]


# 2 : Diffk II

# Given an array A of integers and another non negative integer k, find if there exists 2 indices i and j such that A[i] - A[j] = k, i != j.

# Example :

# Input :

# A : [1 5 3]
# k : 2

# Brute Force approach :
class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return an integer
	def diffPossible(self, A, B):
        K = B
        n = len(A)
        for i in range(n):
            a = A[i]
            b = a - K
            for j in range(i+1, n):
                if A[j] == b:
                    return 1
                j += 1
            i += 1
        return 0

# Optimized solution using HashMap/ Dictionary

class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return an integer
	def diffPossible(self, A, B):
        n = len(A)
        frequencyMap = {}

        for i in range(n):
            if A[i] in frequencyMap:
                frequencyMap[A[i]] += 1
            else:
                frequencyMap[A[i]] = 1

        for i in range(n):
            a = A[i]
            target = a - B
            if target in frequencyMap:
                if (a == target and frequencyMap[a] >= 2 ) :
                    return 1
                elif (a != target and frequencyMap[a] >= 1):
                    return 1
        return 0

# 3 : 2 Sum
# Given an array of integers, find two numbers such that they add up to a specific target number.

# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 < index2. Please note that your returned answers (both index1 and index2 ) are not zero-based. Put both these numbers in order in an array and return the array from your function ( Looking at the function signature will make things clearer ). Note that, if no pair exists, return empty list.

# If multiple solutions exist, output the one where index2 is minimum. If there are multiple solutions with the minimum index2, choose the one with minimum index1 out of them.

# Input: [2, 7, 11, 15], target=9
# Output: index1 = 1, index2 = 2

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def twoSum(self, A, B):
        n = len(A)
        k = B
        frequencyMap = {}
        for i in range(n):
            a = A[i]
            target = k - a

            if target in frequencyMap:
                return frequencyMap[target], i+1
            elif a not in frequencyMap:
                frequencyMap[a] = i+1 
        return []

