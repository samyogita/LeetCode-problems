class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        @cache
        def dac(x, y):
            
            ok = False
            if x == y:
                return True
            for i in range(1, len(x)):
                ok |= dac(x[:i], y[:i]) and dac(x[i:], y[i:])
                ok |= dac(x[:i], y[-i:]) and dac(x[i:], y[:-i])
            return ok
                
        
        return dac(s1,s2)
