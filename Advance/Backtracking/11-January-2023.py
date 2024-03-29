# 1 : Subset
# Given a set of distinct integers A, return all possible subsets.

# NOTE:

# Elements in a subset must be in non-descending order.
# The solution set must not contain duplicate subsets.
# Also, the subsets should be sorted in ascending ( lexicographic ) order.
# The list is not necessarily sorted.


# Problem Constraints
# 1 <= |A| <= 16
# INTMIN <= A[i] <= INTMAX


# Input Format
# First and only argument of input contains a single integer array A.



# Output Format
# Return a vector of vectors denoting the answer.



# Example Input
# Input 1:

# A = [1]
# Input 2:

# A = [1, 2, 3]


# Example Output
# Output 1:

# [
#     []
#     [1]
# ]
# Output 2:

# [
#  []
#  [1]
#  [1, 2]
#  [1, 2, 3]
#  [1, 3]
#  [2]
#  [2, 3]
#  [3]
# ]


# Example Explanation
# Explanation 1:

#  You can see that these are all possible subsets.
# Explanation 2:

# You can see that these are all possible subsets.

class Solution:
	# @param A : list of integers
	# @return a list of list of integers

	def __init__(self):
		self.result = []
	
	def subsets(self, A):
		n = len(A)
		A.sort()
		self.generateSubsets(A, n, [], 0)
		return sorted(self.result)

	def generateSubsets(self, arr, n, currentList, indx):
		if indx == n:
			self.result.append(currentList.copy())
			return
		
		currentList.append(arr[indx])
		self.generateSubsets(arr, n, currentList, indx+1)

		currentList.pop()
		self.generateSubsets(arr, n, currentList, indx+1)


# 2 : Subsets II
# Given a collection of integers denoted by array A of size N that might contain duplicates, return all possible subsets.

# NOTE:

# Elements in a subset must be in non-descending order.
# The solution set must not contain duplicate subsets.
# The subsets must be sorted lexicographically.


# Problem Constraints
# 0 <= N <= 16



# Input Format
# Only argument is an integer array A of size N.



# Output Format
# Return a 2-D vector denoting all the possible subsets.



# Example Input
# Input 1:

#  A = [1, 2, 2]
# Input 2:

#  A = [1, 1]


# Example Output
# Output 1:

#  [
#     [],
#     [1],
#     [1, 2],
#     [1, 2, 2],
#     [2],
#     [2, 2]
#  ]
# Output 2:

#  [
#     [],
#     [1],
#     [1, 1]
#  ]


# Example Explanation
# Explanation 1:

# All the subsets of the array [1, 2, 2] in lexicographically sorted order.

class Solution:
    def __init__(self):
        self.result = []

	def subsetsWithDup(self, A):
        n = len(A)
        A.sort()
        self.generateSubsets(A, n, [], 0)
        return sorted(self.result)

    def generateSubsets(self, arr, n, currentList, indx):
        if indx == n:
            self.result.append(currentList.copy())
            return

        currentList.append(arr[indx])
        self.generateSubsets(arr, n, currentList, indx+1)

        # to ignore duplicate we can compare next element and move pointer to next unique indx 
        while indx < n-1 and arr[indx] == arr[indx+1]:
            indx += 1

        currentList.pop()
        self.generateSubsets(arr, n, currentList, indx+1)


# 3 : Letter Phone

# Given a digit string A, return all possible letter combinations that the number could represent.

# A mapping of digit to letters (just like on the telephone buttons) is given below.



# The digit 0 maps to 0 itself. The digit 1 maps to 1 itself.

# NOTE: Make sure the returned strings are lexicographically sorted.



# Problem Constraints
# 1 <= |A| <= 10



# Input Format
# The only argument is a digit string A.



# Output Format
# Return a string array denoting the possible letter combinations.



# Example Input
# Input 1:

#  A = "23"
# Input 2:

#  A = "012"


# Example Output
# Output 1:

#  ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
# Output 2:

#  ["01a", "01b", "01c"]


# Example Explanation
# Explanation 1:

#  There are 9 possible letter combinations.
# Explanation 2:

#  Only 3 possible letter combinations.

class Solution:
	# @param A : string
	# @return a list of strings
	def letterCombinations(self, A):
        if not A:
            return []
        phonedict = {
            '0': "0",
            '1': "1",
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': 'tuv',
            '9': "wxyz",
        }
        
        N = len(A)
        res = []
        def generateA(index,cur_string):
            if len(cur_string) == N:
                res.append(cur_string)
                return 
            
            number = A[index]
            cur_char = phonedict[number]
            
            for char in cur_char:
                # add char and call the next digit
                generateA(index + 1,cur_string + char)
            
            
             
        generateA(0,"")
        return res 

