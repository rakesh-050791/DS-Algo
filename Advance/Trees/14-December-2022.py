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
