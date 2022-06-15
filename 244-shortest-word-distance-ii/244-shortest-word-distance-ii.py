class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.dic=defaultdict(list)
        #Each key stores all indices of the word
        for i,w in enumerate(wordsDict):
            self.dic[w].append(i)
            

    def shortest(self, word1: str, word2: str) -> int:
        #Get the lists of indices of the two words
        list1,list2=self.dic[word1],self.dic[word2]
        i=j=0
        res=math.inf
        while i<len(list1) and j<len(list2):
            res=min(res,abs(list1[i]-list2[j]))
            #Move pointers in turn
            if list1[i]<list2[j]:
                i+=1
            else:
                j+=1
        return res
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)