# 1 : Spelling Checker

# Given an array of words A (dictionary) and another array B (which contain some words).

# You have to return the binary array (of length |B|) as the answer where 1 denotes that the word is present in the dictionary and 0 denotes it is not present.

# Formally, for each word in B, you need to return 1 if it is present in Dictionary and 0 if not.

# Such problems can be seen in real life when we work on any online editor (like Google Documnet), if the word is not valid it is underlined by a red line.

# NOTE: Try to do this in O(n) time complexity.

# Input Format
# First argument is array of strings A.

# First argument is array of strings B.



# Output Format
# Return the binary array of integers according to the given format.



# Example Input
# Input 1:

# A = [ "hat", "cat", "rat" ]
# B = [ "cat", "ball" ]
# Input 2:

# A = [ "tape", "bcci" ]
# B = [ "table", "cci" ]


# Example Output
# Output 1: [1, 0]
# Output 2: [0, 0]


# Example Explanation
# Explanation 1: Only "cat" is present in the dictionary.
# Explanation 2: None of the words are present in the dictionary.


class TrieNode:
    def __init__(self, char):
        self.char = char
        self.edges = {}
        self.isEnd = False


class Solution:
    def __init__(self):
        self.root = TrieNode(None)

    def solve(self, A, B):
        for word in A:
            self.insert(word)

        result = []

        for char in B:
            if self.search(char):
                result.append(1)
            else:
                result.append(0)
        
        return result
    
    def insert(self, word: str) -> None:
        currentNode = self.root

        for char in word:
            if char not in currentNode.edges:
                currentNode.edges[char] = TrieNode(char)

            currentNode = currentNode.edges[char]

        currentNode.isEnd = True


    def search(self, word: str) -> bool:
        currentNode = self.root

        for char in word:
            if char not in currentNode.edges:
                return False 
            else:
                currentNode = currentNode.edges[char]

        return currentNode.isEnd


# 2 : Shortest Unique Prefix
# Given a list of N words, find the shortest unique prefix to represent each word in the list.

# NOTE: Assume that no word is the prefix of another. In other words, the representation is always possible


# Input Format
# First and only argument is a string array of size N.

# Output Format
# Return a string array B where B[i] denotes the shortest unique prefix to represent the ith word.


# Example Input
# Input 1: A = ["zebra", "dog", "duck", "dove"]
# Input 2: A = ["apple", "ball", "cat"]


# Example Output
# Output 1: ["z", "dog", "du", "dov"]
# Output 2: ["a", "b", "c"]


# Example Explanation
# Explanation 1:

#  Shortest unique prefix of each word is:
#  For word "zebra", we can only use "z" as "z" is not any prefix of any other word given.
#  For word "dog", we have to use "dog" as "d" and "do" are prefixes of "dov".
#  For word "du", we have to use "du" as "d" is prefix of "dov" and "dog".
#  For word "dov", we have to use "dov" as "d" and do" are prefixes of "dog".  
 
# Explanation 2: "a", "b" and c" are not prefixes of any other word. So, we can use of first letter of each to represent.

class TrieNode:
    def __init__(self, char):
        self.char = char
        self.edges = {}
        self.prefixCount = 0

class Solution:
    def __init__(self):
        self.root = TrieNode(None)

    def prefix(self, A):
        for word in A:
            self.insert(word)
        
        result = []

        for word in A:
            response = self.getDistinctPF(word)
            result.append(response)
        
        return result


    def insert(self, word: str) -> None:
        currentNode = self.root

        for char in word:
            if char not in currentNode.edges:
                currentNode.edges[char] = TrieNode(char)
            
            currentNode = currentNode.edges[char]
            currentNode.prefixCount += 1


    def getDistinctPF(self, word: str) -> str:
        currentNode = self.root
        shortestPrefix = ''

        for char in word:
            shortestPrefix += char

            if currentNode.edges[char].prefixCount == 1:
                break
            
            currentNode = currentNode.edges[char]
        
        return shortestPrefix
