from typing import Any
from PyForgeDS.base.LLNode import LLNode

class LinkBasedList:
    def __init__(self):
        self.num_elements = 0
        self.front = None
        self.rear = None
    

    def set(self, index: int, new_element: Any) -> Any:
        if(index < 0 or index >= self.size()):
            raise IndexError("Index out of bounds")

        if index == 0:
            self.getFront().setData(new_element)
            return self.getFront().getData()
        elif index == self.size()-1:
            self.getRear().setData(new_element)
            return self.getRear().getData()
        else:
            current = self.getFront()
            for _ in range(self.size()-1):
                current = current.getNext()

            current.setData(new_element)
            return current.getData()


    def add(self, index: int, element: Any) -> None:
        if(index < 0 or index > self.size()):
            raise IndexError("Index out of bounds")
        
        newNode = LLNode(element)
        if(index == 0):
            if(self.getFront() == None):
                self.setFront(newNode)
                self.setRear(newNode)
            else:
                newNode.setNext(self.getFront())
                self.setFront(newNode)
        elif(index == self.size()):
            next_node = self.getRear().getNext()
            self.getRear().setNext(newNode)
            self.setRear(newNode)
        else:
            current = self.getFront()
            for _ in range(index-1):
                current = current.getNext()

            next_node = current.next
            current.next = newNode
            newNode.next = next_node
        self.num_elements+=1

    def size(self) -> int:
        return self.num_elements

    def isEmpty(self) -> bool:
        return self.num_elements == 0;

    def getFront(self) -> LLNode:
        return self.front
    
    def getRear(self) -> LLNode:
        return self.rear

    def setFront(self, node: LLNode) -> None:
        self.front = node

    def setRear(self, node: LLNode) -> None:
        self.rear = node

    def __iter__(self):
        curr = self.front
        while curr:
            yield curr.data
            curr = curr.next

    def __repr__(self):
        return f"LinkedList([{' -> '.join(repr(x) for x in self)}])"
