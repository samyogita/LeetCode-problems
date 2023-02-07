class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        mp = defaultdict(int)
        l = res = size = 0
        for r in range(len(fruits)):
            if mp[fruits[r]] == 0:
                size += 1
            mp[fruits[r]] += 1
            while size > 2:
                mp[fruits[l]] -= 1
                if not mp[fruits[l]]:
                    size -= 1
                l += 1
            res = max(res, r-l+1)
        return res
