from typing import Any
from PyForgeDS.base.LLNode import LLNode

class LinkBasedQueue:
    def __init__(self) -> None:
        self.element_num: int = 0
        self.front: LLNode = None
        self.rear: LLNode = None

    def enqueue(self, element) -> None:
        newNode = LLNode(element)
        if self.isEmpty():
            self.setFront(newNode)
            self.setRear(newNode)
        else:
            self.getRear().setNext(newNode)
            self.setRear(newNode)
        self.element_num+=1

    def dequeue(self) -> Any:
        if self.isEmpty():
            raise LookupError("Dequeue attempted on Empty Queue")

        prevFront = self.getFront()
        newFront = prevFront.getNext()
        self.setFront(newFront)

        self.element_num-=1
        return prevFront.getData()

    def size(self) -> int:
        return self.element_num

    def isEmpty(self) -> bool:
        return self.element_num == 0

    def getFront(self) -> LLNode:
        return self.front

    def setFront(self, node: LLNode) -> None:
        self.front = node

    def getRear(self) -> LLNode:
        return self.rear
    
    def setRear(self, node: LLNode) -> None:
        self.rear = node

