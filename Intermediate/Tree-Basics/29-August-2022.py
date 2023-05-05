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

# 3 : Nodes Count
# You are given the root node of a binary tree A. You have to find the number of nodes in this tree.



# Problem Constraints
# 1 <= Number of nodes in the tree <= 105

# 0 <= Value of each node <= 107



# Input Format
# The first and only argument is a tree node A.



# Output Format
# Return an integer denoting the number of nodes of the tree.



# Example Input
# Input 1:

#  Values =  1 
#           / \     
#          4   3                        
# Input 2:

 
#  Values =  1      
#           / \     
#          4   3                       
#         /         
#        2                                     


# Example Output
# Output 1:

#  3 
# Output 2:

#  4 


# Example Explanation
# Explanation 1:

# Clearly, there are 3 nodes 1, 4 and 3.
# Explanation 2:

# Clearly, there are 4 nodes 1, 4, 3 and 2.


import sys
sys.setrecursionlimit(10**6)

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, A):
        return self.countNodes(A)

    def countNodes(self, root):
        if root == None:
            return 0

        left = self.countNodes(root.left)
        right = self.countNodes(root.right)

        return 1 + left + right


# 4 : Counting the Nodes

# Given the root of a tree A with each node having a certain value, find the count of nodes with more value than all its ancestor.



# Problem Constraints
# 1 <= Number of Nodes <= 200000

# 1 <= Value of Nodes <= 2000000000



# Input Format
# The first and only argument of input is a tree node.



# Output Format
# Return a single integer denoting the count of nodes that have more value than all of its ancestors.



# Example Input
# Input 1:

 
#      3
# Input 2:

 
#     4
#    / \
#   5   2
#      / \
#     3   6


# Example Output
# Output 1: 1 
# Output 2: 3

# Example Explanation
# Explanation 1:

#  There's only one node in the tree that is the valid node.
# Explanation 2:

#  The valid nodes are 4, 5 and 6.

import sys
sys.setrecursionlimit(10**6)
# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, A):
        return self.countNodes(A, float('-inf'))
    
    def countNodes(self, node, maxx):
        count = 0
        if node == None:
            return 0
        else:
            if node.val > maxx:
                count += 1
            count += self.countNodes(node.left, max(maxx,node.val))
            count += self.countNodes(node.right, max(maxx,node.val))
        
        return count
