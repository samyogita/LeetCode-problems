class UndergroundSystem:

    def __init__(self):
        self.mp1 = {}
        self.mp2 = defaultdict(lambda:(0,0))
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.mp1[id] = (stationName, t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start, t1 = self.mp1[id]
        total, cnt = self.mp2[(start,stationName)]
        total += t - t1
        cnt += 1
        self.mp2[(start,stationName)] = (total, cnt) 

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, cnt = self.mp2[(startStation,endStation)]
        return total / cnt
        
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
