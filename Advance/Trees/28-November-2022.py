# 1 :  Inorder Traversal

# Given a binary tree, return the inorder traversal of its nodes' values.

# NOTE: Using recursion is not allowed.


# Problem Constraints
# 1 <= number of nodes <= 105


# Input Format
# First and only argument is root node of the binary tree, A.

# Output Format
# Return an integer array denoting the inorder traversal of the given binary tree.


# Example Input
# Input 1:

#    1
#     \
#      2
#     /
#    3
# Input 2:

#    1
#   / \
#  6   2
#     /
#    3

# Example Output
# Output 1:

#  [1, 3, 2]
# Output 2:

#  [6, 1, 3, 2]


# Example Explanation
# Explanation 1:

#  The Inorder Traversal of the given tree is [1, 3, 2].
# Explanation 2:

#  The Inorder Traversal of the given tree is [6, 1, 3, 2].

# Solution Using recursion 

# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

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


# Solution using iterative approach, using stacks

from collections import deque
# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param A : root node of tree
	# @return a list of integers
	def inorderTraversal(self, A):
        currentNode = A 
        stack = deque()
        result = []

        while stack or currentNode != None:
            while currentNode != None:
                stack.append(currentNode)
                currentNode = currentNode.left
        
            currentNode = stack[-1]
            stack.pop()
            result.append(currentNode.val)
            currentNode = currentNode.right
        return result


# 2 : Level Order
# Given a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).



# Problem Constraints
# 1 <= number of nodes <= 105



# Input Format
# First and only argument is root node of the binary tree, A.



# Output Format
# Return a 2D integer array denoting the zigzag level order traversal of the given binary tree.



# Example Input
# Input 1:

#     3
#    / \
#   9  20
#     /  \
#    15   7
# Input 2:

#    1
#   / \
#  6   2
#     /
#    3


# Example Output
# Output 1:

#  [
#    [3],
#    [9, 20],
#    [15, 7]
#  ]
# Output 2:

#  [ 
#    [1]
#    [6, 2]
#    [3]
#  ]


# Example Explanation
# Explanation 1:

#  Return the 2D array. Each row denotes the traversal of each level.

from collections import deque
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def levelOrder(self, A):
        myQueue = deque()
        myQueue.append(A)
        result = []

        while myQueue:
            queueSize = len(myQueue)
            level = []

            for _ in range(queueSize):

                currentNode = myQueue.popleft()
                level.append(currentNode.val)
                
                if currentNode.left != None:
                    myQueue.append(currentNode.left)
                
                if currentNode.right != None:
                    myQueue.append(currentNode.right)
            
            if level:
                result.append(level)
    
        return result


# 3 : Left View of Binary tree

# Given a binary tree of integers. Return an array of integers representing the left view of the Binary tree.

# Left view of a Binary Tree is a set of nodes visible when the tree is visited from Left side

# NOTE: The value comes first in the array which have lower level.

# Input Format
# First and only argument is a root node of the binary tree, A.



# Output Format
# Return an integer array denoting the left view of the Binary tree.



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
# Output 1: [1, 2, 4, 8]

# Output 2: [1, 2, 4, 5]


from collections import deque

# Definition for a  binary tree node
class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def solve(self, A):
        myQueue = deque()
        myQueue.append(A)
        result = []

        while myQueue:
            queueSize = len(myQueue)

            for i in range(queueSize):
                currentNode = myQueue.popleft()
                
                if i == 0:
                    result.append(currentNode.val)

                if currentNode.left != None:
                    myQueue.append(currentNode.left)

                if currentNode.right != None:
                    myQueue.append(currentNode.right)

        return result 

# 4 :  Right View of Binary tree
# Given a binary tree of integers denoted by root A. Return an array of integers representing the right view of the Binary tree.

# Right view of a Binary Tree is a set of nodes visible when the tree is visited from Right side


# Input Format
# First and only argument is head of the binary tree A.

# Output Format
# Return an array, representing the right view of the binary tree.



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
# Output 1: [1, 3, 7, 8]
# Output 2: [1, 3, 4, 5]


# Example Explanation
# Explanation 1: Right view is described.

from collections import deque

# Definition for a  binary tree node
class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def solve(self, A):
        myQueue = deque()
        myQueue.append(A)
        result = []

        while myQueue:
            queueSize = len(myQueue)

            for i in range(queueSize):
                currentNode = myQueue.popleft()
                
                if i == queueSize-1:
                    result.append(currentNode.val)

                if currentNode.left != None:
                    myQueue.append(currentNode.left)

                if currentNode.right != None:
                    myQueue.append(currentNode.right)

        return result 
