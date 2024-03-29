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



# 2 : Largest BST Subtree

# You are given a Binary Tree A with N nodes.

# Write a function that returns the size of the largest subtree, which is also a Binary Search Tree (BST).

# If the complete Binary Tree is BST, then return the size of the whole tree.

# NOTE:

# The largest subtree is the subtree with the most number of nodes.

# Input Format
# First and only argument is an pointer to root of the binary tree A.

# Output Format
# Return an single integer denoting the size of the largest subtree which is also a BST.

# Example Input
# Input 1:

#      10
#     / \
#    5  15
#   / \   \ 
#  1   8   7

# Input 2:

#      5
#     / \
#    3   8
#   / \ / \
#  1  4 7  9


# Example Output
# Output 1: 3
# Output 2: 7


# Example Explanation
# Explanation 1:

#  Largest BST subtree is
#                             5
#                            / \
#                           1   8
# Explanation 2:

#  Given binary tree itself is BST.

# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Info:
    def __init__(self, sz, mx, mn, ans, isBST):
        self.sz = sz
        self.mx = int(mx)
        self.mn = int(mn)
        self.ans = ans
        self.isBST = isBST


class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, A):

        res = self.largestBSTinBinaryTree(A)
        return res.ans

    def largestBSTinBinaryTree(self, root):

        if root == None:
            return Info(0, -2e9, 2e9, 0, True)

        if root.left == None and root.right == None:
            return Info(1, root.val, root.val, 1, True)

        l = self.largestBSTinBinaryTree(root.left)
        r = self.largestBSTinBinaryTree(root.right)

        ret = Info(0, 0, 0, 0, True)
        ret.sz = 1 + l.sz + r.sz

        if l.isBST and r.isBST and l.mx < root.val and r.mn > root.val:
            ret.mn = min(l.mn, min(r.mn, root.val))
            ret.mx = max(r.mx, max(l.mx, root.val))
            ret.ans = ret.sz
            ret.isBST = True
            return ret

        ret.ans = max(l.ans, r.ans)
        ret.isBST = False
        return ret


# 3 : Check for BST with One Child

# Given preorder traversal of a binary tree, check if it is possible that it is also a preorder traversal of a Binary Search Tree (BST), where each internal node (non-leaf nodes) have exactly one child.

# Input Format

# First and only argument is an integer array denoting the preorder traversal of binary tree.



# Output Format

# Return a string "YES" if true else "NO".


# Example Input

# Input 1: A : [4, 10, 5, 8]
# Input 2: A : [1, 5, 6, 4]


# Example Output

# Output 1: "YES"
# Output 2: "NO"


# Example Explanation

# Explanation 1:

#  The possible BST is:
#             4
#              \
#              10
#              /
#              5
#               \
#               8
# Explanation 2:

#  There is no possible BST which have the above preorder traversal.

# Solution Approach 

# In Preorder traversal, descendants (or Preorder successors) of every node appear after the node.

# We can say, if all internal nodes have only one child in a BST, then all the descendants of every node are either smaller or larger than the node.

# To check the above condition:

# Scan the last two nodes of preorder & mark them as min & max.

# Scan every node down the preorder array. Each node must be either smaller than the min node or larger than the max node. Update min & max accordingly.

class Solution:
    def solve(self, A):
        n = len(A)
        root = A[0]
        leftMin = float('-inf')
        rightMax = float('inf')

        for i in range(1, n):
            if A[i] > root:
                leftMin = root
            else:
                rightMax = root

            
            if A[i] < leftMin or A[i] > rightMax:
                return 'NO'
            
            root = A[i]
        
        return 'YES'


# 4 : Sorted Array To Balanced BST

# Given an array where elements are sorted in ascending order, convert it to a height Balanced Binary Search Tree (BBST).

# Balanced tree : a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

# Input Format
# First argument is an integer array A.

# Output Format
# Return a root node of the Binary Search Tree.


# Example Input
# Input 1: A : [1, 2, 3]
# Input 2: A : [1, 2, 3, 5, 10]


# Example Output
# Output 1:

#       2
#     /   \
#    1     3
# Output 2:

#       3
#     /   \
#    2     5
#   /       \
#  1         10


# Example Explanation
# Explanation 1: You need to return the root node of the Binary Tree.


# Solution Approach 

# For a BST, all values lower than the root go in the left part of the root, and all values higher go in the right part of the root.
# To balance the tree, we will need to make sure we distribute the elements almost equally in the left and right parts.
# So we choose the mid part of the array as the root and divide the elements around it.

# Things to take care of :
# 1) Are you passing a copy of the array around, or are you only passing around a reference?
# 2) Are you dividing the array before passing it onto the next function call or are you just specifying the start and end index?


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : tuple of integers
    # @return the root node in the tree
    def sortedArrayToBST(self, A):
        n = len(A)
        return self.constructBalancedBST(A, 0, n-1)
  
    def constructBalancedBST(self, A, start, end):
        #base condition
        if start > end:
            return None

        mid = (start + end) // 2
        root = TreeNode(A[mid])

        root.left = self.constructBalancedBST(A, start, mid-1)
        root.right = self.constructBalancedBST(A, mid+1, end)

        return root