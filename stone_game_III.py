class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        score = 0
        n = len(stoneValue)
        @cache 
        def dp(idx):
            if idx == n:
                return 0
            s_one = stoneValue[idx] - dp(idx+1)
            s_two = float('-inf')
            if idx + 2 <= n:
                s_two = stoneValue[idx]+ stoneValue[idx+1] - dp(idx+2)
            s_three = float('-inf')
            if idx + 3 <= n:
                s_three = stoneValue[idx]+ stoneValue[idx+1] +stoneValue[idx+2] - dp(idx+3)
            return max(s_one,s_two,s_three)
        score += dp(0)
        if not score:
            return 'Tie'
        return 'Alice' if score > 0 else 'Bob'

            
            
