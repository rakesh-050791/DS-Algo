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
            
