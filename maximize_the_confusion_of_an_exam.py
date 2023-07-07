class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        l, r = k, len(answerKey)
        
        def isValid(size):
            counter = collections.Counter(answerKey[:size])
            if min(counter['T'], counter['F']) <= k:
                return True
            for i in range(size, len(answerKey)):
                counter[answerKey[i]] += 1
                counter[answerKey[i - size]] -= 1
                if min(counter['T'], counter['F']) <= k:
                    return True
            return False
        
        while l < r:
            mid = (l + r + 1) // 2
            
            if isValid(mid):
                l = mid
            else:
                r = mid - 1
        
        return l
        
