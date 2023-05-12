class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        @cache
        def check(i):
            if i >= len(questions):
                return 0
            include = questions[i][0] + check(i+questions[i][1]+1)
            exclude = check(i+1)
            return max(include,exclude)
        return check(0)
