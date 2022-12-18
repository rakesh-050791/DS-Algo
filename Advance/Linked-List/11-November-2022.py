# 1 : Remove Loop from Linked List
# You are given a linked list that contains a loop.
# You need to find the node, which creates a loop and break it by making the node point to NULL.


# Input Format
# The first of the input contains a LinkedList, where the first number is the number of nodes N, and the next N nodes are the node value of the linked list.
# The second line of the input contains an integer which denotes the position of node where cycle starts.


# Output Format
# return the head of the updated linked list.

# Example Input
# Input 1:
# 1 -> 2
# ^    |
# | - - 

# Input 2:
# 3 -> 2 -> 4 -> 5 -> 6
#           ^         |
#           |         |    
#           - - - - - -

# Example Output
# Output 1: 1 -> 2 -> NULL

# Output 2: 3 -> 2 -> 4 -> 5 -> 6 -> NULL


# Example Explanation
# Explanation 1:

#  Chain of 1->2 is broken.
# Explanation 2:

#  Chain of 4->6 is broken.

# Solution Approach :
# You just need to find what the point is, which has 2 pointers pointing towards it.
# Once you have found it, remove one of the pointers and return the head of the new linked list.

class ListNode:
   def __init__(self, x):
       self.val = x
       self.next = None

class Solution:
    def solve(self, A):
        head = A

        tortoise = hare = head
        isCycle = False

        while hare and hare.next:
            tortoise = tortoise.next
            hare = hare.next.next

            if tortoise == hare:
                isCycle = True
                break

        
        if isCycle is False:
            return None

        s1 = head
        s2 = hare #can be equal to tortoise as well.

        while s1 != s2:
            s1.next
            s2.next

        startOfCycle = s1 #start of cycle 

        while startOfCycle.next != s1:
            startOfCycle = startOfCycle.next 

        startOfCycle.next = None #break cycle here 

        return s1

# 2 : List Cycle

# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

# Try solving it using constant additional space.

# Example:

# Input: 

#                   ______
#                  |     |
#                  \/    |
#         1 -> 2 -> 3 -> 4

# Return the node corresponding to node 3. 

# Solution Approach

# Lets first look at detection of a cycle in the list.

# Following are different ways of doing this

# 1) Use Hashing:
# What if you could maintain a list of nodes already visited. As soon as you visit a node already visited, you know that there is a cycle.

# 2) 2 pointer approach ( Floyd’s Cycle-Finding Algorithm ) :
# What if you have 2 pointers which are going at different speed. For arguments sake, lets just say one pointer is going at double the speed of the other.
# Would they meet if there is a cycle ? Are they guaranteed to meet if there is a cycle ?
# What happens if there is no cycle ?

# Once you detect a cycle, think about finding the starting point.

# Lets now look at the starting point.
# If we were using hashing, the first repetition we get is the starting point. Simple!

# What happens with the 2 pointer approach ?

# Method 1 :
# If you detect a cycle, the meeting point is definitely a point within the cycle.

# Can you determine the size of the cycle ? ( Easy ) Let the size be k.
# Fix one pointer on the head, and another pointer to kth node from head.
# Now move them simulataneously one step at a time. They will meet at the starting point of the cycle.
# Method 2 :
# This might be slightly more complicated. It involves a bit of maths and is not as intuitive as method 1.
# Suppose the first meet at step k,the distance between the start node of list and the start node of cycle is s, and the distance between the start node of cycle and the first meeting node is m.
# Then
# 2k = (s + m + n1r)
# 2(s + m + n2r) = (s + m + n1r)
# s + m = nr where n is an integer.
# s = nr - m
# s = (r - m) + (n-1)r

# So, if we have one pointer on the head and another pointer at the meeting point. Note that since the distance between start node of cycle and the first meeting node is m, therefore if the pointer moves (r - m) steps, it will reach the start of the cycle. When the pointer at the head moves s steps, the second pointer moves (r-m) + (n-1)r steps which both points to the start of the cycle. In other words, both pointers meet first at the start of the cycle.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, A):
        head = A

        slow = fast = head
        cyclePresent = False

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                cyclePresent = True
                break

        s1 = head
        s2 = fast
        if cyclePresent:
            while (s1 != s2):
                s1 = s1.next
                s2 = s2.next
            return s1
        else:
            return None
