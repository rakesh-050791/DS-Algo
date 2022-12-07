# 1 : Vertical Order traversal

# Given a binary tree, return a 2-D array with vertical order traversal of it. Go through the example and image for more details.

# NOTE: If 2 Tree Nodes shares the same vertical level then the one with lesser depth will come first.

# Input Format
# First and only arument is a pointer to the root node of binary tree, A.


# Output Format
# Return a 2D array denoting the vertical order traversal of tree as shown.


# Example Input
# Input 1:

#       6
#     /   \
#    3     7
#   / \     \
#  2   5     9

# Input 2:

#       1
#     /   \
#    3     7
#   /       \
#  2         9


# Example Output
# Output 1:

#  [
#     [2],
#     [3],
#     [6, 5],
#     [7],
#     [9]
#  ]

# Output 2:

#  [
#     [2],
#     [3],
#     [1],
#     [7],
#     [9]
#  ]


# Example Explanation
# Explanation 1: First row represent the verical line 1 and so on.


from collections import deque
# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def verticalOrderTraversal(self, A):
        minLevel = 100000
        maxLevel = 0
        hashmap = dict()
        myQueue = deque()
        myQueue.append((A, 0))

        while myQueue:
            data = myQueue.popleft()
            level = data[1]
            node = data[0]

            if level not in hashmap:
                hashmap[level] = [node.val]
            else:
                hashmap[level].append(node.val)

            minLevel = min(minLevel, level)
            maxLevel = max(maxLevel, level)

            if node.left != None:
                myQueue.append( (node.left , level-1) )

            if node.right != None:
                myQueue.append( (node.right , level+1) )

        result = []

        for i in range(minLevel, maxLevel+1):
            result.append(hashmap[i])
        
        return result


# 2 : Top View of Binary tree

# Given a binary tree of integers denoted by root A. Return an array of integers representing the top view of the Binary tree.

# The top view of a Binary Tree is a set of nodes visible when the tree is visited from the top.

# Return the nodes in any order.


# Input Format
# First and only argument is head of the binary tree A.


# Output Format
# Return an array, representing the top view of the binary tree.


# Example Input
# Input 1:
#             1
#           /   \
#          2    3
#         / \  / \
#        4   5 6  7
#       /
#      8 

# Input 2:
#             1
#            /  \
#           2    3
#            \
#             4
#              \
#               5


# Example Output
# Output 1: [1, 2, 4, 8, 3, 7]
# Output 2: [1, 2, 3]

from collections import deque
# Definition for a  binary tree node
class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution:
    def solve(self, A):
        minLevel = maxLevel = 0
        myQueue = deque()
        myQueue.append((0, A))
        hashmap = {}
        result = []

        while myQueue:
            data = myQueue.popleft()
            level = data[0]
            node = data[1]
            

            minLevel = min(minLevel, level)
            maxLevel = max(maxLevel, level)
            
            if level not in hashmap:
                hashmap[level] = [node.val]
            else:
                hashmap[level].append(node.val)

            if node.left != None:
                myQueue.append((level-1, node.left))
            
            if node.right != None:
                myQueue.append((level+1, node.right))

        
        for i in range(minLevel, maxLevel+1):
            result.append(hashmap[i][0])

        return result


# 3 : Bottom View Of Binary Tree

# Given a Binary Tree A consisting of N integer nodes, you need to print the bottom view from left to right.

# A node x is there in output if x is the bottom-most node at its horizontal distance.

# Horizontal distance of left child of a node x is equal to horizontal distance of x minus 1, and that of right child is horizontal distance of x plus 1.

# Note: If there are multiple bottom-most nodes for a horizontal distance from root, then print the later one in level traversal.


# Input Format

# First and only Argument represents the root of binary tree A.



# Output Format

# Return an one-dimensional integer array denoting the bottom view of A from left to right.



# Example Input

# Input:1
#                       20
#                     /    \
#                   8       22
#                 /   \      \
#               5      3      25
#                     / \      
#                   10    14
# Input:2

#                       20
#                     /    \
#                   8       22
#                 /   \    /   \
#               5      3  4    25
#                     / \      
#                   10    14

# Example Output
# Output:1 : [5, 10, 3, 14, 25]
# Output:2 : [5, 10, 4, 14, 25]


from collections import deque
# Definition for a  binary tree node
class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution:
    def solve(self, A):
        minLevel = maxLevel = 0
        myQueue = deque()
        myQueue.append((0, A))
        hashmap = {}
        result = []

        while myQueue:
            data = myQueue.popleft()
            level = data[0]
            node = data[1]
            

            minLevel = min(minLevel, level)
            maxLevel = max(maxLevel, level)
            
            if level not in hashmap:
                hashmap[level] = [node.val]
            else:
                hashmap[level].append(node.val)

            if node.left != None:
                myQueue.append((level-1, node.left))
            
            if node.right != None:
                myQueue.append((level+1, node.right))

        
        for i in range(minLevel, maxLevel+1):
            result.append(hashmap[i][-1])

        return result


