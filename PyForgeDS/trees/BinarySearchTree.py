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
            return self.recContains(target, node.left)
        if target > node.info:
            return self.recContains(target, node.right)
        
        return True

    def contains(self, target: Any) -> bool:
        return self.recContains(target, self.root)

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

    def recAdd(self, info: Any, node: BSTNode) -> None:
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
        self.node_num+=1

    def recRemove(self, target: Any, node: BSTNode) -> BSTNode:
        if node is None:
            return None

        if target < node.info:
            node.left = self.recRemove(target, node.left)
        elif target > node.info:
            node.right = self.recRemove(target, node.right)
        else:
            # Node with one or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Node with two children
            # Find in-order successor (smallest in right subtree)
            min_larger_node = self._minNode(node.right)
            node.info = min_larger_node.info
            node.right = self.recRemove(min_larger_node.info, node.right)

        return node

    def _minNode(self, node: BSTNode) -> BSTNode:
        while node.left:
            node = node.left
        return node

    def remove(self, target: Any) -> bool:
        if not self.contains(target):
            return False
        self.root = self.recRemove(target, self.root)
        self.node_num-=1
        return True

