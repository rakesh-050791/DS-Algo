# 1 : Double Character Trouble
# You are given a string A.

# An operation on the string is defined as follows:

# Remove the first occurrence of the same consecutive characters. eg for a string "abbcd", the first occurrence of same consecutive characters is "bb".

# Therefore the string after this operation will be "acd".

# Keep performing this operation on the string until there are no more occurrences of the same consecutive characters and return the final string.


# Example Input
# Input 1: A = abccbc
# Input 2: A = ab


# Example Output
# Output 1: "ac"
# Output 2: "ab"


# Example Explanation
# Explanation 1:

# Remove the first occurrence of same consecutive characters. eg for a string "abbc", 
# the first occurrence of same consecutive characters is "bb".
# Therefore the string after this operation will be "ac".

# Explanation 2: No removals are to be done.

# Solution Approach

# Consider an example string abba.
# When we remove the “bb”, the remaining string is “aa” which has to be removed as well.
# So we need to keep track of the characters before the first occurrence of similar consecutive characters.
# We can do this using a stack.
# We keep pushing the characters in a stack, if the current character is equal to the top of the stack,
# we pop from the stack since they represent
# a pair of similar characters.
# Finally, we print the stack in reverse.

from collections import deque

class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        n = len(A)
        myStack = deque()

        for i in range(n):
            if len(myStack) == 0:
                myStack.append(A[i])
            else:
                if A[i] == myStack[-1]:
                    myStack.pop()
                else:
                    myStack.append(A[i])
        print("myStack = ", myStack)
        result = ''.join(myStack)
        return result


# 2 : Evaluate Expression

# An arithmetic expression is given by a string array A of size N. Evaluate the value of an arithmetic expression in Reverse Polish Notation.

# Valid operators are +, -, *, /. Each string may be an integer or an operator.


# Input Format
# The only argument given is string array A.


# Output Format
# Return the value of arithmetic expression formed using reverse Polish Notation.


# Example Input
# Input 1:
#     A =   ["2", "1", "+", "3", "*"]
# Input 2:
#     A = ["4", "13", "5", "/", "+"]

# Example Output
# Output 1: 9
# Output 2: 6


# Example Explanation
# Explaination 1:
#     starting from backside:
#     * : () * ()
#     3 : () * (3)
#     + : (() + ()) * (3)
#     1 : (() + (1)) * (3)
#     2 : ((2) + (1)) * (3)
#     ((2) + (1)) * (3) = 9
# Explaination 2:
#     + : () + ()
#     / : () + (() / ())
#     5 : () + (() / (5))
#     13 : () + ((13) / (5))
#     4 : (4) + ((13) / (5))
#     (4) + ((13) / (5)) = 6


#Solution Approach : 
# When you encounter an operator, that is when you need the top 2 numbers on the stack, perform the operation on them, and put them on the stack.

from collections import deque

class Solution:
    def evalRPN(self, A):
        if len(A) == 1:
            return A[0]

        myStack = deque()
        operators = ['+', '-', '*', '/']

        for i in A:
            if i not in operators:
                myStack.append(i)
            else:
                if (len(myStack) < 2):
                    return -1
                
                # pop the top two elements from the stack, perform the operation 
                # and push that back into the stack

                operand1 = int(myStack.pop())

                operand2 = int(myStack.pop())

                operator = i 

                if operator =='+':
                    myStack.append(operand1 + operand2)
                elif operator =='-':
                    myStack.append(operand2 - operand1)
                elif operator =='*':
                    myStack.append(operand1 * operand2)
                elif operator =='/':
                    myStack.append(int(operand2) / (int(operand1)))

        return int(myStack[0])


# 3 : Infix to Postfix

# Given string A denoting an infix expression. Convert the infix expression into a postfix expression.

# String A consists of ^, /, *, +, -, (, ) and lowercase English alphabets where lowercase English alphabets are operands and ^, /, *, +, - are operators.

# Find and return the postfix expression of A.

# NOTE:

# ^ has the highest precedence.
# / and * have equal precedence but greater than + and -.
# + and - have equal precedence and lowest precedence among given operators.


# Problem Constraints
# 1 <= length of the string <= 500000



# Example Input
# Input 1: A = "x^y/(a*z)+b"

# Input 2: A = "a+b*(c^d-e)^(f+g*h)-i"


# Example Output
# Output 1: "xy^az*/b+"

# Output 2: "abcd^e-fgh*+^*+i-"


# Solution Approach
Algorithm:

# Scan the infix expression from left to right.
# If the scanned character is an operand, output it.
# Else,
# 3.1 If the precedence of the scanned operator is greater than that of the operator in the stack(or the stack is empty, or the stack contains a ‘(‘ ), push it.
# 3.2 Else, Pop all the operators from the stack which are greater than or equal to in precedence than that of the scanned operator. After doing that, Push the scanned operator to the stack. (If you encounter parenthesis while popping, stop there and push the scanned operator in the stack.)
# If the scanned character is an ‘(‘, push it to the stack.
# If the scanned character is an ‘)’, pop the stack and output it until a ‘(‘ is encountered, and discard both the parenthesis.
# Repeat steps 2-6 until infix expression is scanned.
# Print the output
# Pop and output from the stack until it is not empty.


