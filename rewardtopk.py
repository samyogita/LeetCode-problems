class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        mp = defaultdict(int)
        pos = set(positive_feedback)
        neg = set(negative_feedback)
        res = []
        for i in range(len(report)):
            report[i] = report[i].split()
            for item in report[i]:
                if item in pos:
                    mp[student_id[i]] += 3
                if item in neg:
                    mp[student_id[i]] -= 1
        sortmp = sorted(mp.items(), key = lambda x: (-x[1],x[0]))
        for i in range(k):
            res.append(sortmp[i][0])
        return res
        