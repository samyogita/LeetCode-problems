class Solution:
    def compress(self, chars: List[str]) -> int:
        l = i = 0
        while i < len(chars):
            prev = chars[i]
            cnt = 0
            while i < len(chars) and chars[i] == prev:
                i += 1
                cnt += 1
            if cnt > 1:
                chars[l] = prev
                l += 1
                for x in str(cnt):
                    chars[l] = x
                    l += 1
            else:
                chars[l] = prev
                l += 1
        return l


        
            
