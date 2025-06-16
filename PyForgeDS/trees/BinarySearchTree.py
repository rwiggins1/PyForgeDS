from typing import Any
from PyForgeDS.base.BSTNode import BSTNode

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return(self.root == None)

    def min(self):
        raise NotImplementedError()

    def max(self):
        raise NotImplementedError()

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

    def add(self, info):
        if self.root == None:
            self.root = BSTNode(info)
        else:
            self.recAdd(info, self.root)

