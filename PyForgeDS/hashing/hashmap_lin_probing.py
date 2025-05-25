class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
    
class HashMap:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size
    
    def _hash(self, key: any) -> any:
        return hash(key) % self.size
    
    def insert(self, key, value) -> None:
        index = self._hash(key)
        current = self.table[index]
        if current:
            if current.key == key:
                current.val = value
                return
            else:
                while index < self.size: #if bin is filled and key is different, start probing
                    index+=1
                    if index == self.size:
                        self.table.append(Node(key, value))
                        return
                    if not self.table[index]:
                        self.table[index] = Node(key, value)
                        return
        else:
            self.table[index] = Node(key, value)
            return
    
    def get(self, key, *, default_val: any= -1) -> any:
        index = self._hash(key)
        
        while index < self.size:
            if self.table[index].key == key:
                return self.table[index].val
            index+=1
        return default_val

    def delete(self, key) -> bool:
        index = self._hash(key)
        while index < self.size:
            if self.table[index].key == key:
                return True
            index+=1
        return False
    
    def display(self) -> None:
        for i, node in enumerate(self.table):
            if node:
                print(f"Index {i}: ({node.key}: {node.val}),")
            else:
                print(f"Index {i}: NULL")

