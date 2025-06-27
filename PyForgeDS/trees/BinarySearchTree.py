from typing import Any
from PyForgeDS.base.BSTNode import BSTNode

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return(self.root == None)

    def recSize(self, node: BSTNode) -> int:
        raise  NotImplementedError("recSize method not Implemented")

    def size(self) -> int:
        raise  NotImplementedError("Size method not Implemented")

    def recContains(self, target: Any, node: BSTNode) -> bool:
        raise  NotImplementedError("recContains method not Implemented")

    def contains(self, target: Any) -> bool:
        raise  NotImplementedError("Contains method not Implemented")

    def recGet(self, target: Any, node: BSTNode) -> Any:
        if node == None:
            return None
        
        if target < node.info:
            return self.recGet(target, node.left)
        if target > node.info:
            return self.recGet(target, node.right)
        
        return node.info

    def get(self, target: Any) -> Any:
        return self.recGet(target, self.root)
    
    def min(self) -> Any:
        node = self.root

        if self.isEmpty():
            return None
        else:
            while node.left:
                node = node.left
            return node.info

    def max(self) -> Any:
        node = self.root
        
        if self.isEmpty():
            return None
        else:
            while node.right:
                node = node.right
            return node.info

    def recAdd(self, info: Any, node: BSTNode):
        if info < node.info:
            if node.left:
                return self.recAdd(info, node.left)
            else:
                node.left = BSTNode(info)
        if info > node.info:
            if node.right:
                return self.recAdd(info, node.right)
            else:
                node.right = BSTNode(info)

    def add(self, info) -> None:
        if self.isEmpty():
            self.root = BSTNode(info)
        else:
            self.recAdd(info, self.root)

    def recRemove(self, target: Any, node: BSTNode) -> BSTNode:
        raise NotImplementedError("recRemove method not Implemented")
    

    def remove(self, info) -> None:
        raise NotImplementedError("Remove method not Implemented")
