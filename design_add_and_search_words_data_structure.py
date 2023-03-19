class WordDictionary:

    def __init__(self):
        self.mp= defaultdict(WordDictionary)
        self.end = False
        
    def addWord(self, word: str) -> None:
        cur = self
        for x in word:
            cur = cur.mp[x]
        cur.end = True
        

    def search(self, word: str) -> bool:
        cur = self
        for i,x in enumerate(word):
            if x == '.':
                for y in cur.mp.values():
                    if y.search(word[i+1:]):
                        return True
                return False

            if x not in cur.mp:
                return False
            cur = cur.mp[x]
        return cur.end
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
