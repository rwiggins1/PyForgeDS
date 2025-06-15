from PyForgeDS.stacks.ArrayStack import ArrayStack

def test_isEmpty():
    stack = ArrayStack(10)
    assert stack.isEmpty() == True
    stack.push(23)
    stack.push(22)
    assert stack.isEmpty() == False

def test_isFull():
    stack = ArrayStack(2)
    assert stack.isFull() == False
    stack.push(23)
    stack.push(22)
    assert stack.isFull() == True
    
