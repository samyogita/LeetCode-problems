class Solution:
    def smallestString(self, s: str) -> str:
        A = list(s)
        l = 0
        while l < len(s):
            if s[l] != 'a':
                break
            l += 1
        r = l
        while r < len(s):
            if s[r] == 'a':
                break
            r += 1
        for i in range(l, r):
            A[i] = chr(ord(A[i])-1)
        if l == len(s):
            A[-1] = 'z'
        return (''.join(A))
        
