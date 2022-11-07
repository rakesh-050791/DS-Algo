# 1 : Cyclic Permutations

# Given two binary strings A and B, count how many cyclic shift of B when taken XOR with A give 0.

# NOTE: If there is a string, S0, S1, ... Sn-1 , then it is a cyclic shift is of the form Sk, Sk+1, ... Sn-1, S0, S1, ... Sk-1 where k can be any integer from 0 to N-1.


# Example Input
# Input 1:
# A = "1001"
# B = "0011"


# Example Output
# Output 1: 1

# Example Explanation
# Explanation 1:

# 4 cyclic shifts of B exists: "0011", "0110", "1100", "1001".  
#  There is only one cyclic shift of B i.e. "1001" which has 0 xor with A.


# This solution is beased on KMP (Knuth Morris Pratt) Algo. 

class Solution:
    def solve(self, A, B):
        text = A+'@'+B+B
        lps = self.lpsBuilder(text)

        patternlength = len(A)
        result = 0

        for no in lps:
            if no == patternlength:
                result += 1
        
        return result - 1 if A == B else result
        
    
    def lpsBuilder(self, text):
        n = len(text)

        lps = [0] * n

        for i in range(1, n):
            
            x = lps[i-1]
            while (text[i] != text[x]):
            
                if x == 0:
                    x -= 1
                    break
                    
                x = lps[x-1]
                
            lps[i] = x + 1

        return lps
            

# 2 : Hidden Pattern

# Given two strings - a text A and a pattern B, having lower-case alphabetic characters. You have to determine the number of occurrences of pattern B in text A as its substring. i.e. the number of times B occurs as a substring in A.


# Example Input

# Input 1:

#  A = "abababa"
#  B = "aba" 

# Example Output

# Output 1: 3 

# Example Explanation

# Explanation 1:

# A has 3 substrings equal to B - A[1, 3], A[3, 5] and A[5, 7] 

# This solution is beased on KMP (Knuth Morris Pratt) Algo. 

class Solution:
    def solve(self, A, B):
        text = B+'@'+A
        lps = self.lpsBuilder(text)

        patternlength = len(B)
        result = 0

        for no in lps:
            if no == patternlength:
                result += 1
        
        return result
    
    def lpsBuilder(self, text):
        n = len(text)

        lps = [0] * n

        for i in range(1, n):
            
            x = lps[i-1]
            while (text[i] != text[x]):
            
                if x == 0:
                    x -= 1
                    break
                    
                x = lps[x-1]
                
            lps[i] = x + 1

        return lps


# 3 : Smallest Prefix String

# Given 2 strings A and B of size N and M respectively consisting of lowercase alphabets, find the lexicographically smallest string that can be formed by concatenating non-empty prefixes of A and B (in that order).
# Note: The answer string has to start with a non-empty prefix of string A followed by a non-empty prefix of string B.


# Output Format
# Return lexicographically smallest string that can be formed by concatenating non-empty prefixes of A and B (in that order).



# Example Input
# Input 1:

#  A = "abba"
#  B = "cdd"

# Example Output
# Output 1:

#  "abbac"

# Example Explanation
# Explanation 1:

#  We can concatenate prefix of A i.e "abba" and prefix of B i.e "c".
#  The lexicographically smallest string will be "abbac".


# Solution Approach 

# Adding to the hint, we keep appending characters from the first string till the current character is less than the first character of the second string.
# After that, we add the first character of the second string, and we have our answer.
# (Since we want the lexicographically smallest string)

# Time Complexity:- O(A)

class Solution:
    def smallestPrefix(self, A, B):

        outputStr = A[0]+''

        # keep appending A[i] till it is smaller than B[0]
        for i in range(1, len(A)):
            if ord(A[i]) < ord(B[0]):
                outputStr += A[i]
            else:
                break

        return outputStr + B[0]