from typing import Any
from PyForgeDS.base.BSTNode import BSTNode

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.node_num = 0

    def isEmpty(self):
        return(self.root == None)

    def size(self) -> int:
        return self.node_num

    def recContains(self, target: Any, node: BSTNode) -> bool:
        if node == None:
            return False
        
        if target < node.info:
            return self.recContains(target, node.getLeft())
        if target > node.info:
            return self.recContains(target, node.getRight())
        
        return True

    def contains(self, target: Any) -> bool:
        return self.recContains(target, self.getHead())

    def recGet(self, target: Any, node: BSTNode) -> Any:
        if node == None:
            return None
        
        if target < node.info:
            return self.recGet(target, node.getInfo())
        if target > node.info:
            return self.recGet(target, node.getRight())
        
        return node.info

    def get(self, target: Any) -> Any:
        return self.recGet(target, self.getHead())
    
    def min(self) -> Any:
        node = self.getHead()

        if self.isEmpty():
            return None
        else:
            while node.getLeft():
                node = node.getLeft()
            return node.getInfo()

    def max(self) -> Any:
        node = self.getHead()
        
        if self.isEmpty():
            return None
        else:
            while node.getRight():
                node = node.getRight()
            return node.getInfo()

    def recAdd(self, info: Any, node: BSTNode) -> None:
        if info < node.getInfo():
            if node.getLeft():
                return self.recAdd(info, node.getLeft())
            else:
                node.left = BSTNode(info)
        if info > node.getInfo():
            if node.getRight():
                return self.recAdd(info, node.getRight())
            else:
                node.right = BSTNode(info)

    def add(self, info) -> None:
        if self.isEmpty():
            self.root = BSTNode(info)
        else:
            self.recAdd(info, self.getHead())
        self.node_num+=1

    def recRemove(self, target: Any, node: BSTNode) -> BSTNode:
        if node is None:
            return None

        if target < node.getInfo():
            node.left = self.recRemove(target, node.getLeft())
        elif target > node.getInfo():
            node.right = self.recRemove(target, node.getRight())
        else:
            # Node with one or no child
            if node.left is None:
                return node.getRight()
            elif node.right is None:
                return node.getLeft()

            # Node with two children
            # Find in-order successor (smallest in right subtree)
            min_larger_node = self._minNode(node.getRight())
            node.setInfo(min_larger_node)
            node.setRight(self.recRemove(min_larger_node.getInfo(), node.getRight()))

        return node

    def _minNode(self, node: BSTNode) -> BSTNode:
        while node.getLeft():
            node = node.getLeft()
        return node

    def remove(self, target: Any) -> bool:
        if not self.contains(target):
            return False
        self.root = self.recRemove(target, self.getHead())
        self.node_num-=1
        return True

    def getHead(self) -> BSTNode:
        return self.root

