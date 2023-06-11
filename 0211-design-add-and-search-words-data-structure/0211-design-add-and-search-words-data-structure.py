class WordNode:
    def __init__(self):
        self.children={}
        self.isWord=False
class WordDictionary:

    def __init__(self):
        self.root=WordNode()

    def addWord(self, word: str) -> None:
        curr=self.root
        for w in word:
            if w not in curr.children:
                curr.children[w]=WordNode()
            curr=curr.children[w]
        curr.isWord=True

    def search(self, word: str) -> bool:
        # when we have '.', we basically want to compare the remaining string with all children of the current level
        # use a stack. Push new pairs onto the stack for comparision
        stack=[(self.root,word)]
        while stack:
            curr,w=stack.pop()
            if not w:
                if curr.isWord:
                    return True
            elif w[0]=='.':
                # push all children onto the stack
                for c in curr.children.values():
                    stack.append((c,w[1:]))
            else:
                if w[0] in curr.children:
                    node=curr.children[w[0]]
                    stack.append((node,w[1:]))
        return False
        

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)