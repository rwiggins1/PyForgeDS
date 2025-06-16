from typing import Any

class BSTNode:
    def __init__(self, info: Any):
        self.info = info
        self.left = None
        self.right = None
        
    def __repr__(self):
            return f"BSTNode({self.info}, left={self.left}, right={self.right})"
