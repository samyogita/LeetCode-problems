from collections import defaultdict

class Trie:
    def __init__(self):
        self.mp = defaultdict(Trie)
        self.end = False
        
    

    def insert(self, word: str) -> None:
        cur = self
        for x in word:
           cur = cur.mp[x]
        cur.end = True

    def search(self, word: str) -> bool:
        cur = self
        for x in word:
            if x not in cur.mp:
                return False
            cur = cur.mp[x]
        return cur.end
        

    def startsWith(self, prefix: str) -> bool:
        cur = self
        for x in prefix:
            if x not in cur.mp:
                return False
            cur = cur.mp[x]
        return True
        

