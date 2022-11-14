# 1 :Merge Two Sorted Lists

# Merge two sorted linked lists, A and B, and return it as a new list.

# The new list should be made by splicing together the nodes of the first two lists and should also be sorted.


# Input Format
# The first argument of input contains a pointer to the head of linked list A.

# The second argument of input contains a pointer to the head of linked list B.

# Output Format
# Return a pointer to the head of the merged linked list.



# Example Input
# Input 1:

#  A = 5 -> 8 -> 20
#  B = 4 -> 11 -> 15

# Example Output
# Output 1: 4 -> 5 -> 8 -> 11 -> 15 -> 20

# Example Explanation
# Explanation 1: Merging A and B will result in 4 -> 5 -> 8 -> 11 -> 15 -> 20 

# Solution Approach 

# The first thing to note is that all you would want to do is modify the next pointers. You don’t need to create new nodes.

# At every step, you choose the minimum of the current head X on the 2 lists and modify your answer’s next pointer to X. You move the current pointer on the said list and the current answer.

# Corner case,
# Make sure that at the end of the loop, when one of the lists goes empty, you do include the remaining elements from the second list into your answer.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, A, B):
        list1 = A
        list2 = B

        if list1 is None:
            return list2
        
        if list2 is None:
            return list1

        newHead = None

        #preparing new head node
        if (list1.val < list2.val):
            newHead = list1
            list1 = list1.next
        else:
            newHead = list2
            list2 = list2.next
        
        temp = newHead

        #Compairing both LL in increasing order and moving pointers to get a merged LL
        while (list1 != None and list2 != None):
            if (list1.val < list2.val):
                temp.next = list1
                list1 = list1.next
                temp = temp.next
            else:
                temp.next = list2
                list2 = list2.next
                temp = temp.next

        # Linking remaining nodes
        if list1 != None:
            temp.next = list1
        
        if list2 != None:
            temp.next = list2

        return newHead


Solution 2 : Using Dummy Linkedlist 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def mergeTwoLists(self, A, B):
        headA = A
        headB = B
        dummy = ListNode(0)
        dummy_head = dummy
        while (headA is not None) and (headB is not None):
            if headA.val < headB.val:
                dummy.next = ListNode(headA.val)
                headA = headA.next
                dummy = dummy.next
            else:
                dummy.next = ListNode(headB.val)
                headB = headB.next
                dummy = dummy.next
        if headA is not None:
            dummy.next = headA
        elif headB is not None:
            dummy.next = headB
        return dummy_head.next