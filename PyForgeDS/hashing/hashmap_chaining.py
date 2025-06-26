from typing import Any
from PyForgeDS.base.LLNode import HM_LLNode as Node

def abc_case(letter: str) -> int:
    abc = {
        "a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7,
        "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16,
        "q": 17, "r": 18, "s": 19,
        "t": 20, "u": 21, "v": 22,
        "w": 23, "x": 24,
        "y": 25, "z": 26
    }
    return abc[letter]

class hashMap:
    def __init__(self, orig_cap=10):
        self.orig_cap = orig_cap
        self.table = [None] * orig_cap  # Initialize empty table
        self.num_pairs = 0
    
    def _hash(self, key: Any) -> Any:
        return hash(key) % self.orig_cap

    def __enlarge(self) -> None:
        raise NotImplementedError("enlarge method for HashMap not implemented")
    
    def put(self, key, value: int) -> None:
        index = self._hash(key)
        self.num_pairs+=1
        
        if self.table[index]:
            # Collision
            current = self.table[index]
            while current:
                if current.key == key: # Replace
                    current.value = value
                    return

                if current.next is None:
                    current.next = Node(key, value)
                    return
                current = current.next
        
        self.table[index] = Node(key, value)
        return
    
    def get(self, key: Any, *, default_value: Any = -1) -> Any:
        index = self._hash(key)
        
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return default_value
    
    def remove(self, key: Any) -> bool:
        index = self._hash(key)
        current = self.table[index]
        prev = None
        
        while current:
            if current.key == key:
                if prev is None:
                    self.table[index] = current.next
                else:
                    prev.next = current.next
                self.num_pairs-=1
                return True
            prev = current
            current = current.next
        return False
    
    # check if key exist
    def contains(self, key: Any) -> bool:
        if self.isEmpty():
            return False
        
        index = self._hash(key)
        current = self.table[index]

        while current:
            if current.key == key:
                return True
            current = current.next
        return False

    def isEmpty(self) -> bool:
        return(self.num_pairs == 0)
    
    # is never empty
    def isFull(self) -> bool:
        return False

    def size(self) -> int:
        return self.num_pairs

    def display(self) -> None:
        for i, node in enumerate(self.table):
            print(f"{i}:", end=" ")
            current = node
            while current:
                print(f"({current.key}: {current.value}) ->", end=" ")
                current = current.next
            print("None")

