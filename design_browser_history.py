class BrowserHistory:
    def __init__(self, homepage: str):
        self.ls = [homepage]
        self.pos = 0
        self.last = 0
        
    def visit(self, url: str) -> None:
        self.pos += 1
        if self.pos == len(self.ls):
            self.ls.append(url)
        else:
            self.ls[self.pos] = url
        self.last = self.pos
        
    def back(self, steps: int) -> str:
        if self.pos < steps:
            self.pos = 0
        else:
            self.pos -= steps 
        return self.ls[self.pos]
        
    def forward(self, steps: int) -> str:
        if self.pos + steps > self.last:
            self.pos = self.last
        else:
            self.pos += steps
        return self.ls[self.pos]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
