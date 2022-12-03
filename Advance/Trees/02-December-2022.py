# 1 : Valid Binary Search Tree

# You are given a binary tree represented by root A.

# Assume a BST is defined as follows:

# 1) The left subtree of a node contains only nodes with keys less than the node's key.

# 2) The right subtree of a node contains only nodes with keys greater than the node's key.

# 3) Both the left and right subtrees must also be binary search trees.

# Output Format
# Return 0 if false and 1 if true.



# Example Input
# Input 1:
 
#    1
#   /  \
#  2    3

# Input 2:

#   2
#  / \
# 1   3

# Example Output
# Output 1: 0
# Output 2: 1

# Example Explanation
# Explanation 1: 2 is not less than 1 but is in left subtree of 1.
# Explanation 2: Satisfies all conditions.

# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param A : root node of tree
	# @return an integer
	def isValidBST(self, A):
        start = float('-inf')
        end = float('inf')
        root = A

        result =  self.validBST(root, start, end)
        return 1 if result else 0

    
    def validBST(self, root, start, end):
        if root == None:
            return True
        
        if start <= root.val and root.val <= end:
            lst = self.validBST(root.left, start, root.val - 1)
            rst = self.validBST(root.right, root.val+1, end)
            return lst and rst
        else:
            return False
