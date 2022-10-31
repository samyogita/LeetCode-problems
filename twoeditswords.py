class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        res = []
        for q in queries:
            for d in dictionary:
                def check(q, d):
                    count = 0
                    for x, y in zip(q, d):
                        if x != y:
                            count += 1
                    return count <= 2
        
                if check(q,d):
                    res.append(q)
                    break
        return res
                