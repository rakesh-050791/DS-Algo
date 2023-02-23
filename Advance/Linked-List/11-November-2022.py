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

# 3 : Reorder List 

# Given a singly linked list A

#  A: A0 → A1 → … → An-1 → An 
# reorder it to:

#  A0 → An → A1 → An-1 → A2 → An-2 → … 
# You must do this in-place without altering the nodes' values.



# Problem Constraints
# 1 <= |A| <= 106



# Input Format
# The first and the only argument of input contains a pointer to the head of the linked list A.



# Output Format
# Return a pointer to the head of the modified linked list.



# Example Input
# Input 1:

#  A = [1, 2, 3, 4, 5] 
# Input 2:

#  A = [1, 2, 3, 4] 


# Example Output
# Output 1: [1, 5, 2, 4, 3] 
# Output 2: [1, 4, 2, 3] 


# Example Explanation
# Explanation 1: The array will be arranged to [A0, An, A1, An-1, A2].
# Explanation 2: The array will be arranged to [A0, An, A1, An-1, A2].

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reorderList(self, A):
        if A.next == None or A.next.next == None:
            return A

        head = A

        slow = fast = head
        fromm = None

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        secondLL = slow.next
        slow.next = None

        reversedSecondLL = self.reverseLL(secondLL)

        current1 = head
        current2 = reversedSecondLL

        while current1 and current2:
            next1 = current1.next
            next2 = current2.next

            current1.next = current2
            current2.next = next1

            current1 = next1
            current2 = next2

        return head
    
    def reverseLL(self, head):
        temp = head
        headOfReverseLL = None

        while head != None:
            temp = head
            head = head.next
            temp.next = None
            temp.next = headOfReverseLL
            headOfReverseLL = temp
        
        return headOfReverseLL

# 4 : Intersection of Linked Lists
# Write a program to find the node at which the intersection of two singly linked lists, A and B, begins. For example, the following two linked lists:

# A:          a1 → a2
#                    ↘
#                      c1 → c2 → c3
#                    ↗
# B:     b1 → b2 → b3
# NOTE:

# If the two linked lists have no intersection at all, return null.
# The linked lists must retain their original structure after the function returns.
# You may assume there are no cycles anywhere in the entire linked structure.
# Your code should preferably run in O(n) time and use only O(1) memory.
# The custom input to be given is different than the one explained in the examples. Please be careful.


# Problem Constraints

# 0 <= |A|, |B| <= 106



# Input Format

# The first argument of input contains a pointer to the head of the linked list A.

# The second argument of input contains a pointer to the head of the linked list B.



# Output Format

# Return a pointer to the node after which the linked list is intersecting.



# Example Input

# Input 1:

#  A = [1, 2, 3, 4, 5]
#  B = [6, 3, 4, 5]
# Input 2:

#  A = [1, 2, 3]
#  B = [4, 5]


# Example Output

# Output 1:

#  [3, 4, 5]
# Output 2:

#  []


# Example Explanation

# Explanation 1:

#  In the first example, the nodes have the same values after 3rd node in A and 2nd node in B. Thus, the linked lists are intersecting after that point. 
# Explanation 2:

#  In the second example, the nodes don't have the same values, thus we can return None/Null. 


'''
Definition for singly-linked list
class ListNode:
   def __init__(self, val):
      self.val = val
      self.next = None
'''
class Solution:
    def getIntersectionNode(self, A, B):
        list1 = A
        list2 = B

        list1_len = 0
        list2_len = 0

        cur = list1
        while cur:
            list1_len += 1
            cur = cur.next

        cur = list2
        while cur:
            list2_len += 1
            cur = cur.next

        bigger_list, smaller_list = (A, B) if list1_len > list2_len else (B, A)

        len_diff = abs(list1_len-list2_len)

        # Advance bigger list by difference 
        while len_diff > 0:
            len_diff -= 1
            bigger_list = bigger_list.next

        # Both the lists are at same level when advanced and checked, should meet
        # if they are connected
        while bigger_list and smaller_list:
            if bigger_list == smaller_list:
                return bigger_list
            bigger_list = bigger_list.next
            smaller_list = smaller_list.next

        return None