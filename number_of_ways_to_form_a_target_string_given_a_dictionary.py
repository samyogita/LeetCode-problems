class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10 ** 9 + 7
        cnt = [Counter(x[i] for x in words)for i in range(len(words[0]))]
        @cache
        def dp(i,j):
            if i == len(target):
                return 1
            if j == len(words[0]):
                return 0
            include = dp(i+1,j+1) * cnt[j][target[i]]
            exclude = dp(i, j+1)
            return (include+exclude)

        return dp(0,0) % MOD
