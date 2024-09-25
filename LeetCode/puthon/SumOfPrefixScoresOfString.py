from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.count = 0

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        root = TrieNode()
        
        for word in words:
            node = root
            for char in word:
                node = node.children[char]
                node.count += 1

        result = []

        for word in words:
            node = root
            score = 0
            for char in word:
                node = node.children[char]
                score += node.count
            result.append(score)

        return result


