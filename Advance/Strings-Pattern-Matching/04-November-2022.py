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


# 4 : Closest Palindrome

# Groot has a profound love for palindrome which is why he keeps fooling around  with strings.
# A palindrome string is one that reads the same backward as well as forward.

# Given a string A of size N consisting of lowercase alphabets, he wants to know if it is possible to make the given string a palindrome by changing exactly one of its character.


# Output Format
# Return the string YES if it is possible to make the given string a palindrome by changing exactly 1 character. Else, it should return the string NO.



# Example Input
# Input 1:

# A = "abbba"

# Output 1: "YES"


# Example Explanation
# Explanation 1:

#  We can change the character at index 3(1-based) to any other character. The string will be palindromic.


# Solution Approach 

# We apply our standard palindrome checking algorithm and count the number of times a set of mirror indices has different characters.
# If at the end of processing, this count is greater than 1, then it can never be possible since we will have to change more than one character to make it a palindrome.
# If the count is 1, the answer is always yes.
# A corner case that needs to be considered is the case when the count is 0.
# If the count is 0 and the palindrome length is even, then we cannot change exactly one character to make it a palindrome. We will have to change two mirror indices.
# But if the count is 0 and the length is odd, then it is possible as we can change the middlemost character to anything.

class Solution:
    def solve(self, A):

        n = len(A)
        count = 0
        
        i , j = 0, n-1

        while i < j:
            if A[i] != A[j]:
                count += 1

            if count > 1:
                return 'NO'                
            
            i += 1
            j -= 1
        
        if count == 1:
            return 'YES'

        if count == 0:
            if n % 2 == 0:
                return 'NO'
            else:
                return 'YES'


# 5 : Make String Palindrome

# Given a string A of size N consisting only of lowercase alphabets. The only operation allowed is to insert characters in the beginning of the string.

# Find and return how many minimum characters are needed to be inserted to make the string a palindrome string.

# Output Format
# Return an integer denoting the minimum characters needed to be inserted in the beginning to make the string a palindrome string.


# Example Input
# Input 1:

# A = "abc"
 
# Example Output
# Output 1: 2


# Example Explanation
# Explanation 1:

#  Insert 'b' at beginning, string becomes: "babc".
#  Insert 'c' at beginning, string becomes: "cbabc".


#Solution Approach 

# Each index of the LPS array contains the longest prefix, which is also a suffix. Now take the string and reverse of a string and combine them with a sentinel character in between them and compute the LPS array of this combined string. Now take the last value of the LPS array and subtract it from the length of the original string. This will give us the minimum number of insertions required at the beginning of the string.

class Solution:
    def solve(self, A):
        n = len(A)
        reverseA = A[::-1]
        text = A +'@'+ reverseA
        lps = self.lpsBuilder(text)
        # lps array contains the longest prefix, which is also a suffix
        longestPalindromeLen = lps[-1] #lps[2*n]

        return n - longestPalindromeLen


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


# 6 : Period of a string

# You are given a string A of length N consisting of lowercase alphabets. Find the period of the string.

# Period of the string is the minimum value of k (k >= 1), that satisfies A[i] = A[i % k] for all valid i.


# Example Input
# Input 1:

#  A = "abababab"
# Input 2:

#  A = "aaaa"


# Example Output
# Output 1:

#  2
# Output 2:

#  1


# Example Explanation
# Explanation 1:

#  Period of the string will be 2: 
#  Since, for all i, A[i] = A[i%2]. 
# Explanation 2:

#  Period of the string will be 1.


# Solution explanation 

# Since the period of a string is a substring 
# which repeats itself to form the string 
# after a point lps values will increase by 1.

# Example → ‘ab’ is the period of the string 
# ‘abababab’ where it repeats 4 times to form the string.
# However, ‘abab’ is also a period of this string 
# as it repeats 2 times to form the string.

# In this question we have to find the smallest period 
# of the string. So, the answer is ‘ab’ i.e. 2. 

# Now, there are two cases which we will encounter - 

# Case 1: When we have a perfect string 
# A perfect string would be a string where, the period 
# will multiply itself an exact number of times.

# Example - ‘ababab’ 
# Here ‘ab’ is repeated thrice. 

# Case 2: When we don’t have a perfect string
# Example - ‘abcaabcaab’
# Here ‘abca’ is repeated twice and then only ‘ab’ is 
# appended at the end. So, this is not a perfect 
# string. However the period is still ‘abca’ i.e. 4. 

# In both the cases the final LPS value will give us 
# the total characters in the string - length of the period. 
# It is because, the KMP algorithm calculates the LPS for 
# proper prefix and proper suffix and so the length of the 
# period will always be excluded because if we add it then 
# the highest LPS will be equal to the string length and 
# hence it won’t be considered a proper prefix or a suffix. 

# Thus, the answer is straightforward. The last value of the 
# lps array would give us the value of string length - period, 
# so we just subtract that value from the string length. 

class Solution:
    def solve(self, A):
        n = len(A)
        lps = self.lpsBuilder(A)

        return n - lps[n-1]

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
