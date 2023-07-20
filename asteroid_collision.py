class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for a in asteroids:
            if not stack or a > 0:
                stack.append(a)
            else:
                while stack and stack[-1] > 0 and stack[-1] < abs(a):
                    stack.pop()

                if stack and stack[-1] == abs(a):
                    stack.pop()
                else:
                    if not stack or stack[-1] < 0:
                        stack.append(a)
        
        return stack
