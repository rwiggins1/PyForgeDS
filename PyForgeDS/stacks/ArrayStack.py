from typing import Any

class ArrayStack:
    def __init__(self, max_size=100):
        self.max_size = max_size
        self.array = [None] * max_size
        self.top_index = -1

    def isEmpty(self) -> bool:
        return(self.top_index == -1)
    
    def isFull(self) -> bool:
        return(self.top_index == self.max_size-1)

    def push(self, element: Any) -> None:
        if self.isFull():
            raise OverflowError("Push attempted on a full stack")
        else:
            self.top_index+=1 
            self.array[self.top_index] = element

    def pop(self) -> Any:
        raise NotImplementedError("Pop method not implemented")

    def top(self) -> None:
        if self.isEmpty():
            raise LookupError("Top attempted on Empty Stack")
        else:
            return self.array[self.top_index]

