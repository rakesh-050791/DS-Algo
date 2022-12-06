# 1 : Least Common Ancestor

# Find the lowest common ancestor in an unordered binary tree A, given two values, B and C, in the tree.

# Lowest common ancestor: the lowest common ancestor (LCA) of two nodes and w in a tree or directed acyclic graph (DAG) is the lowest (i.e., deepest) node that has both v and w as descendants.

# Input Format
# First argument is head of tree A.

# Second argument is integer B.

# Third argument is integer C.

# Output Format
# Return the LCA.

# Example Input
# Input 1:

#       1
#      /  \
#     2    3
#    / \
#   4   5
# B = 4
# C = 5


# Example Output
# Output 1: 2


# Example Explanation
# Explanation 1: LCA is 2.

# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param A : root node of tree
	# @param B : integer
	# @param C : integer
	# @return an integer
	def lca(self, A, B, C):
        pathB = []
        pathC = []
        x = self.getPath(A, B, pathB)
        y = self.getPath(A, C, pathC)

        if x == False or y == False:
            return -1

        i = 0 

        while i < len(pathB) and i < len(pathC):
            if pathB[i] != pathC[i]:
                break
            i += 1

        return pathB[i-1]

    
    def getPath(self, root, k, path):
        if root == None:
            return False
        
        path.append(root.val)
        
        if root.val == k:
            return True

        if (root.left != None and self.getPath(root.left, k, path)) or (root.right != None and self.getPath(root.right, k, path)):
            return True
        
        path.pop()
        return False
