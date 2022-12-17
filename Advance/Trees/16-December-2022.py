# 1 :  Path Sum

# Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.


# Input Format
# First argument is a root node of the binary tree, A.

# Second argument is an integer B denoting the sum.



# Output Format
# Return 1, if there exist root-to-leaf path such that adding up all the values along the path equals the given sum. Else, return 0.



# Example Input
# Input 1:

#  Tree:    5
#          / \
#         4   8
#        /   / \
#       11  13  4
#      /  \      \
#     7    2      1

#  B = 22
# Input 2:

#  Tree:    5
#          / \
#         4   8
#        /   / \
#      -11 -13  4

#  B = -1


# Example Output
# Output 1: 1
# Output 2: 0


# Example Explanation
# Explanation 1: There exist a root-to-leaf path 5 -> 4 -> 11 -> 2 which has sum 22. So, return 1.
# Explanation 2: There is no path which has sum -1.

# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param A : root node of tree
	# @param B : integer
	# @return an integer
	def hasPathSum(self, A, B):
        root = A 
        return self.dfs(A, 0, B)
        # currentSum = B 
    
    def dfs(self, root, currentSum, B):

        if not root:
            return 0

        currentSum += root.val

        if not root.left and not root.right:
            return 1 if (currentSum == B) else 0

        return (self.dfs(root.left, currentSum, B) or self.dfs(root.right, currentSum, B))
