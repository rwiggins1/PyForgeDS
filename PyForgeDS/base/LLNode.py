from typing import Any

class LLNode:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

    def getData(self) -> Any:
        return self.data

    def getNext(self) -> Any:
        return self.next
    
    def setData(self, data) -> None:
        self.data = data

    def setNext(self, node) -> None:
        self.next = node

class HM_LLNode:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        self.next = None
