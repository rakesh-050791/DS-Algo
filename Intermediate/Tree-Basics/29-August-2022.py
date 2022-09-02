# 1 : Tree Height

# You are given the root node of a binary tree A. You have to find the height of the given tree.

# A binary tree's height is the number of nodes along the longest path from the root node down to the farthest leaf node.


import sys
sys.setrecursionlimit(10**6)

class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, A):
        root = A 

        if root == None:
            return 0
        
        left = self.solve(root.left)
        right = self.solve(root.right)

        return 1 + max(left, right)


# 2 :  Inorder Traversal
# Given a binary tree, return the inorder traversal of its nodes values.
# Input :
# 	1
#   / \
#  6   2
#     /
#    3
# Output :  [6, 1, 3, 2]

import sys
sys.setrecursionlimit(10**6)

class Solution:
	# @param A : root node of tree
	# @return a list of integers
	def inorderTraversal(self, A):
        result = []
        self.inOrder(A, result)
        return result
        
    def inOrder(self, root, result):
        if root == None:
            return

        if root.left:
            self.inOrder(root.left, result)
            
        result.append(root.val)            

        if root.right:
            self.inOrder(root.right, result)