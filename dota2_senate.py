from collections import Counter, deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        cnt = Counter(senate)
        rcnt = dcnt =  0
        q = deque(senate)
        while cnt['D'] and cnt['R']:
            cur = q.popleft()
            if cur == 'D':
                if rcnt > 0:
                    cnt[cur] -= 1
                    rcnt -= 1
                else: 
                    dcnt += 1
                    q.append(cur)
            else:
                if dcnt > 0:
                    cnt[cur] -= 1
                    dcnt -= 1
                else:
                    rcnt += 1
                    q.append(cur)

        return 'Radiant' if cnt['D'] == 0 else 'Dire'
