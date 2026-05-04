class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.arr = []

    def get(self, i: int) -> int:
        return self.arr[i]


    def set(self, i: int, n: int) -> None:
        self.arr[i] = n


    def pushback(self, n: int) -> None:
        self.length += 1
        if self.length > self.capacity:
            self.resize()
        self.arr.append(n)


    def popback(self) -> int:
        self.length -= 1
        return self.arr.pop()
 

    def resize(self) -> None:
        self.capacity *= 2


    def getSize(self) -> int:
        return self.length
        
    
    def getCapacity(self) -> int:
        return self.capacity
