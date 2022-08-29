class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mp = [0] * 26
        for i in ransomNote:
            pos = ord(i) - ord('a')
            mp[pos] += 1
        print(mp)
        mp2 = [0] * 26        
        for k in magazine:
            pos = ord(k) - ord('a')
            mp2[pos] += 1
        print(mp2)        
        for i in range(0, 26):
            if mp2[i] < mp[i]:
                return False
            
        return True
        