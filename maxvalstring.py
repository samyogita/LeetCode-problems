class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        mx = 0
        for ele in strs:
            flag = True
            for i in ele:
                if i.isalpha():
                    flag = False
                    break

            if flag:
                mx = max(mx, int(ele))
            else:
                mx = max(mx, len(ele))
        return mx