class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        saved_result = {}
        def compute_cost(i, j):

            if i < 0 and j < 0:
                return 0
            if (i, j) in saved_result:
                return saved_result[(i, j)]
            
            if i < 0:
                saved_result[(i, j)] = ord(s2[j]) + compute_cost(i, j-1)
                return saved_result[(i, j)]
            if j < 0:
                saved_result[(i, j)] = ord(s1[i]) + compute_cost(i-1, j)
                return saved_result[(i, j)]
            
            if s1[i] == s2[j]:
                saved_result[(i, j)] = compute_cost(i-1, j-1)
            else:
                saved_result[(i, j)] = min(
                    ord(s1[i]) + compute_cost(i-1, j),
                    ord(s2[j]) + compute_cost(i, j-1)
                )

            return saved_result[(i, j)]

        return compute_cost(len(s1)-1, len(s2)-1)
