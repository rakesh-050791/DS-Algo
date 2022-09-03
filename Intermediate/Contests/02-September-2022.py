# 1 : Given a sequence f(A) = f(A-1) + f(A-2) + f(A-3) + A. 
# Calculate the Ath term of the sequence. Given f(0)=1; f(1)=1; f(2)=2;
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        
        if A == 0 or A == 1:
            return 1
        elif A == 2:
            return 2
        else:
            return ( self.solve(A-1) + self.solve(A-2) + self.solve(A-3) + A)



    
#     def mySplit(self, str):
#         arr = [0, 0]
#         head = str.rstrip('0123456789')
#         tail = str[len(head):]
#         arr[0] = head
#         arr[1] = tail
#         return arr