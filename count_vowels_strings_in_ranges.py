def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        res = []
        vowels = {'a', 'e', 'i', 'o', 'u'}
        for x in words:
            if (x[0] in vowels and x[-1] in vowels):
                res.append(1)
            else:
                res.append(0)
        pre = [0]
        arr = []
        for k in res:
            pre.append(pre[-1]+k)
        for i,j in queries:
            arr.append(pre[j+1]-pre[i])
            
        return arr
                
