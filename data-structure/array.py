from typing import List


class array:
    def __init__(self) -> List:
        self.length = 0
        self.data = {}

    def __str__(self) -> str:
        print(self.data.values())
        return str(self.__dict__)

    def get(self, index):
        return self.data[index]

    def push(self, item):
        self.length += 1
        self.data[self.length - 1] = item

    def pop(self):
        temp = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return temp

    def insert(self, idx, item):
        self.length += 1
        for i in range(self.length - 1, idx, -1):
            self.data[i] = self.data[i - 1]
        self.data[idx] = item

    def delete(self, idx):
        for i in range(self.length - 1, idx, -1):
            self.data[i - 1] = self.data[i]
        del self.data[self.length - 1]
        self.length -= 1


if __name__ == "__main__":

    a = array()
    a.push(1)
    a.push(2)
    a.push(3)
    a.push(4)
    a.push(5)
    print(a)

    a.pop()
    print(a)

    a.delete(2)
    print(a)

    a.insert(2, 10)
    print(a)
