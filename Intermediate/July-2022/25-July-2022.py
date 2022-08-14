						# Bit Manipulations

# 1 : Help From Sam 

# Alex and Sam are good friends. Alex is doing a lot of programming these days. He has set a target score of A for himself.
# Initially, Alex's score was zero. Alex can double his score by doing a question, or
# Alex can seek help from Sam for doing questions that will contribute 1 to Alex's score. 
# Alex wants his score to be precisely A. Also, he does not want to take much help from Sam.
# Find and return the minimum number of times Alex needs to take help from Sam to achieve a score of A.

# Solution 

# Hint 1 : When A = 5
# The Question Says 
# 1. Alex can double his score by doing a question, or 
# 2. Alex can seek help from Sam for doing questions that will contribute 1 to Alex’s score. 
# 3. Alex wants his score to be precisely A.

# So assume Alex score initially is 0. Now to reach it to A say 5 we have two solution
# 1. Either Alex can double his score by doing a question. But 2x0 = 0.
# 2. Or Alex can seek help from Sam. So 0+ 1= 1, 
# 3. After this Alex can double his score by doing a question. So, 1x2 =2
# 4. Again, Alex can double his score by doing a question. Since in question it is mention “Alex does not want to take much help from Sam”. So, 2x2 =4
# 5. Now Alex has to take help from Sam so that 4+1=5 which is A.
# If we go for other condiotion in which Alex double his score by doing a question then. 4x2 =8 which is not A. So that is why he need Sam’s help.

# So finally we can tell how many times Alex has taken help by using counter viz., two times from above observation


# Hint 2 : when A = 7 
# There will be 4 1’s where alex need to take help from Sam. 
# Step 1: Alex take help (0 + 1).
# Step 2: Alex will do on his own (1 * 2 = 2)
# Step 3 :  Alex take help (2 + 1).
# Step 4: Alex will do on his own (3 * 2 = 6)
# Step 5: Alex take help (6 + 1).

# The number of times Alex took help is 3

# Basically the idea behind the solution is to check the no of set bits in given integer


class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):

        numberOfSetBits = 0

        while (A > 0):
            if A & 1 == 1:
                numberOfSetBits += 1
            
            A = A >> 1
        return numberOfSetBits

# 2 :

