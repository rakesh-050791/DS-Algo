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
