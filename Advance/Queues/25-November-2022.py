# 1 : First non-repeating character

# Given a string A denoting a stream of lowercase alphabets, you have to make a new string B.
# B is formed such that we have to find the first non-repeating character each time a character is inserted to the stream and append it at the end to B. If no non-repeating character is found, append '#' at the end of B.


# Input Format
# The only argument given is string A.


# Output Format
# Return a string B after processing the stream of lowercase alphabets A.


# Example Input
# Input 1: A = "abadbc"

# Input 2: A = "abcabc"


# Example Output
# Output 1: "aabbdd"

# Output 2: "aaabc#"

# Example Explanation

# Explanation 1:
# "a"      -   first non repeating character 'a'
# "ab"     -   first non repeating character 'a'
# "aba"    -   first non repeating character 'b'
# "abad"   -   first non repeating character 'b'
# "abadb"  -   first non repeating character 'd'
# "abadbc" -   first non repeating character 'd'

# Explanation 2:
# "a"      -   first non repeating character 'a'
# "ab"     -   first non repeating character 'a'
# "abc"    -   first non repeating character 'a'
# "abca"   -   first non repeating character 'b'
# "abcab"  -   first non repeating character 'c'
# "abcabc" -   no non repeating character so '#'

# Solution Approach :

# You need to maintain a map for each character of the stream.
# After that, you can also maintain a queue for the extraction of information.
# Each character is inserted and removed from the queue at most once; hence time complexity is O(n).

from collections import deque

class Solution:
    def solve(self, A):
        n = len(A)
        hashMap = {}
        myQueue = deque()
        resultStr = ''

        for char in A:
            if char not in hashMap:
                hashMap[char] = 1
                # if char ocuring for the first time, insert in queue
                myQueue.append(char)
            else:
                hashMap[char] += 1

            while myQueue and hashMap[myQueue[0]] > 1:
                myQueue.popleft()
            
            if myQueue:
                resultStr += myQueue[0]
            else:
                resultStr += '#'
        
        return resultStr

