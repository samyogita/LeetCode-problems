class Solution:
    def isValid(self, s: str) -> bool:
        open = {"(":")", "{":"}", "[":"]"}
        opposite = {"}", "]", ")"}
        stack = []
    
        for i in s:
            if i in open:
                stack.append(open[i])
            elif i in opposite:
                if not stack or stack.pop() != i:
                    return False

        return len(stack) == 0