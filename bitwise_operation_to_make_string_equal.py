from collections import Counter
class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        arr = zip(s, target)
        pairs = Counter(arr)
        print(pairs)
        if s == target:
            return True
        for i in range(len(s)):
            if s[i] == '1' and target[i] == '1':
                return True
            
        if pairs[('1', '0')] >= 1 and pairs[('0', '1')] >= 1:
            return True
        
        return False