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


# Solution 2 : Using Dummy Linkedlist 

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

# 2 : Palindrome List

# Given a singly linked list A, determine if it's a palindrome. Return 1 or 0, denoting if it's a palindrome or not, respectively.

# Output Format
# Return 0, if the linked list is not a palindrome.

# Return 1, if the linked list is a palindrome.

# Example Input
# Input 1:

# A = [1, 2, 2, 1]
# Input 2:

# A = [1, 3, 2]

# Example Output
# Output 1: 1 
# Output 2: 0 

# Example Explanation
# Explanation 1:

#  The first linked list is a palindrome as [1, 2, 2, 1] is equal to its reversed form.
# Explanation 2:

#  The second linked list is not a palindrom as [1, 3, 2] is not equal to [2, 3, 1].


class ListNode:
  def __init__(self, x):
      self.val = x
      self.next = None

cclass Solution:
    def lPalin(self, A):
        if A.next == None:
            return 1
        
        middleNode = self.getMid(A) 
        list2 = middleNode.next
        middleNode.next = None

        head1 = A
        head2 = self.reverseLL(list2)

        return self.compareTwoLL(A, head2)

    def reverseLL(self, listHead):
        reversedLLHead = None

        while listHead != None:
            temp = listHead
            listHead = listHead.next
            temp.next = None #breaking link from existing linkedList 
            temp.next = reversedLLHead #adding link to a new linkedList 
            reversedLLHead = temp
        
        return reversedLLHead

    def getMid(self, A):
        slow = fast = A

        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def compareTwoLL(self, headOne, HeadTwo):
        while headOne and HeadTwo:
            if headOne.val != HeadTwo.val:
                return 0
            headOne = headOne.next
            HeadTwo = HeadTwo.next
        return 1


# 3 : Clone a Linked List


# Given a doubly linked list of integers with one pointer of each node pointing to the next node (just like in a single link list) while the second pointer, however, can point to any node in the list and not just the previous node.

# You have to create a copy of this list and return the head pointer of the duplicated list.


# Input Format
# The only argument given is head pointer of the doubly linked list.

# Output Format
# Return the head pointer of the duplicated list.


# Example Input
# Input 1:

# 1 -> 2 -> 3 -> 4 -> 5
# random pointer of each node 
# 1 -> 5 2 -> 4 3 -> 3 4 -> 2 5 -> 1

# Example Output
# Output 1:

# 1 -> 2 -> 3 -> 4 -> 5
# random pointer of each node 
# 1 -> 5 2 -> 4 3 -> 3 4 -> 2 5 -> 1


# Example Explanation
# Explanation 1: Just clone the given list.

"""
class ListNode: 
    def __init__(x):
        self.val = x
        self.next = None
        self.random = None
"""
def clonelist(A):
    head1 = A
    temp1 = A 
    
    # STEP 1 : Cloning list1 head1 into list2 head2
    while (temp1 != None):
        # print("temp1 = ", temp1.val)
        temp2 = ListNode(temp1.val)
        temp2.next = temp1.next
        temp1.next = temp2
        temp1 = temp2.next  #temp1.next.next

    
    head2 = head1.next
    temp1 = head1
    temp2 = head2

    # STEP 2 : list2 is ready from STEP 1, now filling random pointers for list 2
    while (temp1 != None):
        temp2.random = temp1.random.next
        temp1 = temp2.next

        if temp1 == None:
            break

        temp2 = temp1.next
            

    temp1 = head1
    temp2 = head2

    # STEP 3 : filling next pointers in list1 and list2 (correct next linking)
    while (temp1 != None):
        temp1.next = temp2.next
        temp1 = temp1.next

        if temp1 == None:
            break
            
        temp2.next = temp1.next
        temp2 = temp2.next
            
    return head2


# 4 : LRU Cache

# Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.

# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# set(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least recently used item before inserting the new item.
# The LRUCache will be initialized with an integer corresponding to its capacity. Capacity indicates the maximum number of unique keys it can hold at a time.

# Definition of "least recently used" : An access to an item is defined as a get or a set operation of the item. "Least recently used" item is the one with the oldest access time.

# NOTE: If you are using any global variables, make sure to clear them in the constructor.

# Example :

# Input : 
#          capacity = 2
#          set(1, 10)
#          set(5, 12)
#          get(5)        returns 12
#          get(1)        returns 10
#          get(10)       returns -1
#          set(6, 14)    this pushes out key = 5 as LRU is full. 
#          get(5)        returns -1 

Solution Approach :

# Lets approach this question bit by bit.
# If lets say you never had to remove entries from the LRU cache because we had enough space, what would you use to support and get and set ?
# A simple map / hashmap would suffice.

# Alright, lets now look at the second part which is where the eviction comes in. We need a data structure which at any given instance can give me the least recently used objects in order. Lets see if we can maintain a linked list to do it. We try to keep the list ordered by the order in which they are used. So whenever, a get operation happens, we would need to move that object from a certain position in the list to the front of the list. Which means a delete followed by insert at the beginning.

# Insert at the beginning of the list is trivial. How do we achieve erase of the object from a random position in least time possible ?

# How about we maintain another map which stores the pointer to the corresponding linked list node.

# Ok, now when we know the node, we would need to know its previous and next node in the list to enable the deletion of the node from the list. We can get the next in the list from next pointer ? What about the previous node ? To encounter that, we make the list doubly linked list.


# As discussed in the previous hint, we solve this problem using :

# originalMap : A hashmap which stores the orginial key to value mapping
# accessList : A doubly linked list which has keys ordered by their access time ( Most recently used key in front of the list to least recently used key at the end of the list ).
# addressMap : A hashmap which saves the mapping of key to address of the key in accessList.
# Lets see now how the get and set operation would work :

# get(key) :
# Look for the value corresponding to key in originalMap.
# If key is not found, we don’t need to change accessList. So, return -1.
# If key is found, then we need to move the node corresponding to the key to front of the list in accessList.
# To do that, we find the address of the node for key from addressMap. We make the node->prev->next = node->next;, node->next->prev = node->prev;, node->prev = NULL; node->next = head; head->prev = node;
# We update the head of the accessList to be node now.

# set(key, value)
# If the key is a new entry (it does not exist in the originalMap) AND the cache is full(size = capacity), then we would need to remove the least recently used key lkey.
# We know that this key is the key corresponding to the last node in accessList which is accessible in O(1). To evict, we delete the last node from accessList, and the entry corresponding to lkey(from last node) in addressMap and originalMap.

# Post this, there are 2 cases.

# key is a new entry and is not present in originalMap. In this case, a new node is created for key and inserted at the head of accessList. A new (key,value) entry is created into originalMap and addressMap accordingly.
# key is present in the map, in which case the value needs to be updated. We update the value in the originalMap and then we update the accessList for key exactly the way we did in the case of get operation.
# A couple of insights for clean code :

# Note that the update of accessList for key when key is present is a common operation in get and a subcase of set function. We should create a function for it and call that function in both cases to reduce redundancy.
# Also, note that originalMap and addressMap are always of the same size with the same keys ( One with value and the other with address in linkedlist ). If you want to manage less maps, you can just have a masterMap which maps key to a pair of (value, address_in_list)

class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)

        self.head.next = self.tail
        self.tail.prev = self.head

        self.cache = {}

    # @return an integer
    def get(self, key):
        if key not in self.cache:
            return -1
        else:
            node = self.cache[key]
            self.deleteNode(node)
            self.addAtTail(node)
            return node.val

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        newNode = Node(key, value)

        if key in self.cache:
            node = self.cache[key]
            self.deleteNode(node)
            self.addAtTail(newNode)
        else:
            if len(self.cache) == self.capacity:
                self.deleteNode(self.head.next)
                self.addAtTail(newNode)
            else:
                self.addAtTail(newNode)

    def deleteNode(self, node):
        tp = node.prev
        tn = node.next

        tp.next = tn
        tn.prev = tp

        node.prev = None
        node.next = None

        del self.cache[node.key]

    def addAtTail(self, node):
        tp = self.tail.prev
        tp.next = node
        node.prev = tp
        node.next = self.tail
        self.tail.prev = node
        self.cache[node.key] = node


# 5 : Sort List

# Sort a linked list, A in O(n log n) time using constant space complexity.

# Input Format
# The first and the only arugment of input contains a pointer to the head of the linked list, A.

# Output Format
# Return a pointer to the head of the sorted linked list.



# Example Input
# Input 1:

# A = [3, 4, 2, 8]
# Input 2:

# A = [1]


# Example Output
# Output 1:

# [2, 3, 4, 8]
# Output 2:

# [1]


# Example Explanation
# Explanation 1:

#  The sorted form of [3, 4, 2, 8] is [2, 3, 4, 8].
# Explanation 2:

#  The sorted form of [1] is [1].

sys.setrecursionlimit(10**6)

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:    
    def getMidNode(self, A):
        if A.next.next == None:
            return A
        
        slow = fast = A

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
    
    def sortList(self, A):
        if A == None or A.next == None:
            return A

        middleNode = self.getMidNode(A)
        
        head1 = A 
        head2 = middleNode.next

        middleNode.next = None

        list1 = self.sortList(head1)
        list2 = self.sortList(head2)

        return self.merge(list1, list2)

    def merge(self, list1, list2):
        newHead = None

        if list1.val < list2.val:
            newHead = list1
            list1 = list1.next
        else:
            newHead = list2
            list2 = list2.next
        
        temp = newHead

        while (list1 is not None) and (list2 is not None):
            if list1.val < list2.val:
                temp.next = ListNode(list1.val)
                list1 = list1.next
            else:
                temp.next = ListNode(list2.val)
                list2 = list2.next
            
            temp = temp.next

        if list1 is not None:
            temp.next = list1
        elif list2 is not None:
            temp.next = list2
        
        return newHead

# 6 : Flatten a linked list

# Given a linked list where every node represents a linked list and contains two pointers of its type:

# Pointer to next node in the main list (right pointer)
# Pointer to a linked list where this node is head (down pointer). All linked lists are sorted.
# You are asked to flatten the linked list into a single list. Use down pointer to link nodes of the flattened list. The flattened linked list should also be sorted.



# Problem Constraints
# 1 <= Total nodes in the list <= 100000

# 1 <= Value of node <= 109



# Input Format
# The only argument given is head pointer of the doubly linked list.



# Output Format
# Return the head pointer of the Flattened list.



# Example Input
# Input 1:

#    3 -> 4 -> 20 -> 20 ->30
#    |    |    |     |    |
#    7    11   22    20   31
#    |               |    |
#    7               28   39
#    |               |
#    8               39
# Input 2:

#    2 -> 4 
#    |    |       
#    7    11    
#    |            
#    7


# Example Output
# Output 1:

#  3 -> 4 -> 7 -> 7 -> 8 -> 11 -> 20 -> 20 -> 20 -> 22 -> 28 -> 30 -> 31 -> 39 -> 39 
# Output 2:

#  2 -> 4 -> 7 -> 7 -> 11


# Example Explanation
# Explanation 1:

#  The return linked list is the flatten sorted list.

 """
class ListNode:
    def __init__(self,x):
        self.val=x
        self.right=None
        self.down=None
"""
import sys
sys.setrecursionlimit(10**9)
# @param root: ListNode
# @return ListNode
def flatten(root):
    if not root or not root.right:
        return root
    mid = get_mid(root)
    h1 = root
    h2 = mid.right
    mid.right = None
    l1 = flatten(root)
    l2 = flatten(h2)
    return merge2Lists(l1, l2)

def get_mid(root):
    if not root or not root.right:
        return root
    slow, fast = root, root
    while fast.right and fast.right.right:
        slow, fast = slow.right, fast.right.right
    return slow

def merge2Lists(h1, h2):
    if not h1 and not h2:
        return h1
    elif not h1:
        return h2
    elif not h2:
        return h1
    if h1.val <= h2.val:
        h1.down = merge2Lists(h1.down, h2)
        return h1
    else:
        h2.down = merge2Lists(h1, h2.down)
        return h2
        
