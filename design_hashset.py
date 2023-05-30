class MyHashSet:

    def __init__(self):
        self.list = []
        

    def add(self, key: int) -> None:
        if key not in self.list:
            self.list.append(key)
        

    def remove(self, key: int) -> None:
        if key in self.list:
            self.list.remove(key)

        

    def contains(self, key: int) -> bool:
        if key in self.list:
            return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
