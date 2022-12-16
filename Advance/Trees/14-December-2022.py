# 1 : Invert the Binary Tree

# Given a binary tree A, invert the binary tree and return it.

# Inverting refers to making the left child the right child and vice versa.

# Input Format
# First and only argument is the head of the tree A.

# Output Format
# Return the head of the inverted tree.


# Example Input
# Input 1:

 
#      1
#    /   \
#   2     3
# Input 2:

 
#      1
#    /   \
#   2     3
#  / \   / \
# 4   5 6   7


# Example Output
# Output 1:

 
#      1
#    /   \
#   3     2
# Output 2:

 
#      1
#    /   \
#   3     2
#  / \   / \
# 7   6 5   4


# Example Explanation
# Explanation 1:

# Tree has been inverted.
# Explanation 2:

# Tree has been inverted.

# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param A : root node of tree
	# @return the root node in the tree
	def invertTree(self, A):
        if not A:
            return None

        temp = A.left
        A.left = A.right
        A.right = temp
        self.invertTree(A.left)
        self.invertTree(A.right)
        
        return A


# 2 : Equal Tree Partition

# Given a binary tree A. Check whether it is possible to partition the tree to two trees which have equal sum of values after removing exactly one edge on the original tree.


# Input Format
# First and only argument is head of tree A.


# Output Format
# Return 1 if the tree can be partitioned into two trees of equal sum else return 0.



# Example Input
# Input 1:

 
#                 5
#                /  \
#               3    7
#              / \  / \
#             4  6  5  6
# Input 2:

 
#                 1
#                / \
#               2   10
#                   / \
#                  20  2


# Example Output
# Output 1:

#  1
# Output 2:

#  0


# Example Explanation
# Explanation 1:

# Remove edge between 5(root node) and 7: 
#         Tree 1 =                                               Tree 2 =
#                         5                                                     7
#                        /                                                     / \
#                       3                                                     5   6    
#                      / \
#                     4   6
# Sum of Tree 1 = Sum of Tree 2 = 18

# Explanation 2: The given Tree cannot be partitioned.


# Definition for a  binary tree node
class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

import sys
sys.setrecursionlimit(1500)

class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, A):
        return self.checkEqualPartition(A)

    def checkEqualPartition(self, A):
        hashSet = set()

        summ = self.dfs(A, hashSet)

        if summ % 2:
            return 0 
        
        if summ // 2 in hashSet:
            return 1
        return 0
        
    def dfs(self, root, hashSet):
        if not root:
            return 0 
        
        currentSum = root.val + self.dfs(root.left, hashSet) + self.dfs(root.right, hashSet)
        
        hashSet.add(currentSum)

        return currentSum


# 3 : Kth Smallest Element In BST

# Given a binary search tree represented by root A, write a function to find the Bth smallest element in the tree.

# Input Format
# First and only argument is head of the binary tree A.

# Output Format
# Return an integer, representing the Bth element.


# Example Input
# Input 1:

 
#             2
#           /   \
#          1    3
# B = 2
# Input 2:

 
#             3
#            /
#           2
#          /
#         1
# B = 1



# Example Output
# Output 1: 2
# Output 2: 1


# Example Explanation
# Explanation 1: 2nd element is 2.
# Explanation 2: 1st element is 1.



# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
    hashMap = {}
    hashMap[None] = 0

	def kthsmallest(self, A, B):
        self.generateHashMap(A)

        current = A 
        while (current is not None):
            if self.hashMap[current.left] == B-1:
                return current.val
            elif (B <= self.hashMap[current.left]):
                current = current.left
            else:
                B = B - self.hashMap[current.left] - 1
                current = current.right 

        return -1
            
    def generateHashMap(self, root):
        if not root:
            return 0
        
        l = self.generateHashMap(root.left)
        r = self.generateHashMap(root.right)

        self.hashMap[root] = l + r + 1

        return l + r + 1
