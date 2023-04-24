class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            f = stones.pop()
            s = stones.pop()
            if f != s:
                stones.append(f-s)
        return 0 if not stones else stones[0]
        
            
                
        
            
        
