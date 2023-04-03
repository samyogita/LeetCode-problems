class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        cnt = 0
        people.sort()
        l = 0
        r = len(people)-1
        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1
            r -= 1
            cnt += 1
                
        return cnt
            
