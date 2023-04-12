class Solution:
    def simplifyPath(self, path: str) -> str:
        s = path.split('/')
        res = []
        for i in s:
            if i == '..':
                if res:
                    res.pop()
            elif i != '.' and len(i) > 0:
                res.append(i)

        return '/' + '/'.join(res)
