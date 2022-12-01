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

