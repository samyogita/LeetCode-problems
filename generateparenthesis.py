class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def backtrack(openN, closedN, stack):
            if openN == closedN == n:
                res.append(''.join(stack))
                return
            
            if openN < n:
                
                backtrack(openN + 1, closedN, stack + ['('])
                
            
            if closedN < openN:
                
                backtrack(openN, closedN + 1, stack + [')'])
                
            
        
        backtrack(0, 0, [])
        return res