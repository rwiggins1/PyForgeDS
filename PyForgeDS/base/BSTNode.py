from typing import Any

class BSTNode:
    def __init__(self, info: Any):
        self.info = info
        self.left = None
        self.right = None

    def getInfo(self) -> Any:
        return self.info
    
    def getLeft(self) -> Any:
        return self.left
    
    def getRight(self) -> Any:
        return self.right
        
    def __repr__(self):
            return f"BSTNode({self.info}, left={self.left}, right={self.right})"
