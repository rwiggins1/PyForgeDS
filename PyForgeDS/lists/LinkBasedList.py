from typing import Any
from PyForgeDS.base.LLNode import LLNode

class LinkBasedList:
    def __init__(self):
        self.num_elements = 0
        self.front = None
        self.rear = None
    
    def size(self) -> int:
        return self.num_elements

    def set(self, index: int, new_element: Any):
        if(index < 0 or index > self.size()):
            raise IndexError("Index out of bounds")

        raise NotImplementedError("Set method not finished")

    def add(self, index: int, element: Any) -> None:
        raise NotImplementedError("Add method not implemented")

