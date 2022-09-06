class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordset=set(wordList)
        dq=collections.deque([(beginWord,1)])
        while dq:
            word,length=dq.popleft()
            if word==endWord:
                return length
            for i in range(len(word)):
                for c in 'qwertyuiopasdfghjklzxcvbnm':
                    newWord=word[:i]+c+word[i+1:]
                    if newWord in wordset:
                        dq.append((newWord,length+1))
                        wordset.remove(newWord)
        return 0