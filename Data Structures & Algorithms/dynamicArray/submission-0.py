class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.array = [0] * self.capacity

    def get(self, i: int) -> int:
        if 0 <= i < self.size:
            return self.array[i]

    def set(self, i: int, n: int) -> None:
        if 0 <= i < self.size:
            self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.capacity *= 2
            new_array = [0] * self.capacity
            for i in range(self.size):
                new_array[i] = self.array[i]
            self.array = new_array

        self.array[self.size] = n
        self.size += 1

    def popback(self) -> int:
        self.size -= 1
        return self.array[self.size]
 

    def resize(self) -> None:
        self.capacity *= 2

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity
