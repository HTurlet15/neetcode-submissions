class Pair:
    def __init__(self,key,val):
        self.key = key
        self.val = val

class HashTable:
    
    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.map = [None]*capacity

    def hash(self, key: int):
        return key%self.capacity

    def insert(self, key: int, value: int) -> None:
        index = self.hash(key)
        
        while True :
            if self.map[index] == None:
                self.map[index] = Pair(key,value)
                self.size +=1
                if self.size >= self.capacity //2:
                    self.resize()
                return
            if self.map[index].key == key:
                self.map[index].val = value
                return
            index += 1
            index = index % self.capacity


    def get(self, key: int) -> int:
        index = self.hash(key)

        while self.map[index] != None:
            if self.map[index].key == key:
                return self.map[index].val
            index += 1
            index = index % self.capacity
        return -1

    def remove(self, key: int) -> bool:
        hash_index = self.hash(key)
        index = hash_index

        while self.map[index]!=None:
            if self.map[index].key == key:
                self.map[index] = None
                self.size = self.size - 1
                self.open_adress(hash_index, index)
                return True
            index+=1
            index = index % self.capacity
        return False

    def open_adress(self, hash_index, index) -> None:
        while True :
            next_index = (index+1)%self.capacity
            if self.map[next_index]==None:
                return

            next_key = self.map[next_index].key
            if self.hash(next_key) != hash_index :
                return
                
            self.map[index] = self.map[next_index]
            next_index = (index+1)%self.capacity

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        self.capacity = self.capacity * 2

        oldMap = self.map
        self.map = [None] * self.capacity
        self.size = 0

        for pair in oldMap :
            if pair != None :
                self.insert(pair.key, pair.val)

