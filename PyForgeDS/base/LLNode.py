class LLNode:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class HM_LLNode:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        self.next = None
