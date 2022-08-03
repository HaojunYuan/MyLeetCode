class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res,counter=0,collections.Counter(chars)
        for word in words:
            wordCounter=collections.Counter(word)
            for c in wordCounter:
                if wordCounter[c]>counter[c]:
                    break
            else:
                res+=len(word)
        return res
                
        # sum, chars_counter = 0, collections.Counter(chars)
        # for word in words:
        #     word_counter = collections.Counter(word)
        #     for c in word_counter:
        #         if word_counter[c] > chars_counter[c]:
        #             break
        #     else:
        #         sum += len(word)
        # return sum