class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, string):
        curr = self.root
        for c in string:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
            curr.count += 1

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        myTrie = Trie()
        for s in strs:
            myTrie.insert(s)
        curr = myTrie.root
        res = ''
        for c in strs[0]:
            if c in curr.children:
                curr = curr.children[c]
                if curr.count == len(strs):
                    res += c
                else:
                    break
        return res