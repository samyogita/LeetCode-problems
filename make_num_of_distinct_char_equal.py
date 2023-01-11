from collections import Counter
class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        a = Counter(word1)
        b = Counter(word2)
        for i, x in a.items():
            mp1 = a.copy()
            mp2 = b.copy()
            mp1[i] -= 1 
            mp2[i] += 1
            for j, y in b.items():
                mp1[j] += 1
                mp2[j] -= 1  
                cnt1 = sum(1 if mp1[x] > 0 else 0 for x in mp1.keys())
                cnt2 = sum(1 if mp2[x] > 0 else 0 for x in mp2.keys())
                if cnt1 == cnt2:
                    return True
                mp1[j] -= 1 
                mp2[j] += 1
            mp1[i] += 1 
            mp2[i] -= 1
        return False
            