class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        res = []
        k = celsius + 273.15
        f = (celsius * 1.80) + 32.00
        k = "{0:.5f}".format(k)
        f = "{0:.5f}".format(f)
        res.append(float(k))
        res.append(float(f))
        return res
        