class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def check(s, t):
            mp = dict()
            for i, j in zip(s,t):
                if i in mp:
                    if mp[i] != j:
                        return False
                mp[i] = j
            return True
        return check(s,t) and check(t, s)