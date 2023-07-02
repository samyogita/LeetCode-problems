class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        for i in range(len(requests),0,-1):
            for c in itertools.combinations(range(len(requests)),i):
                deg = [0] * n
                for val in c:
                    deg[requests[val][0]] -= 1
                    deg[requests[val][1]] += 1
                if not any(deg):
                    return i
        return 0 
