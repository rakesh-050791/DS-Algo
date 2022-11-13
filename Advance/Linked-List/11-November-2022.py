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

