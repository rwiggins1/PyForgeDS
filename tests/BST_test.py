from PyForgeDS.trees.BinarySearchTree import BinarySearchTree

def test_isEmpty():
    bst = BinarySearchTree()
    assert bst.isEmpty() == True

def test_add():
    bst = BinarySearchTree()
    bst.add(12)
    assert bst.getHead().getInfo()== 12
    bst.add(10)
    assert bst.getHead().getLeft().getInfo() == 10
    bst.add(94)
    assert bst.getHead().getRight().getInfo() == 94

def test_min_max():
    bst = BinarySearchTree()
    bst.add(12)
    assert bst.getHead().getInfo() == 12
    bst.add(10)
    assert bst.getHead().getLeft().getInfo() == 10
    bst.add(94)
    assert bst.getHead().getRight().getInfo() == 94
    bst.add(3)
    assert bst.min() == 3
    bst.add(100)
    assert bst.max() == 100

def test_get():
    bst = BinarySearchTree()
    assert bst.get(3) == None
    bst.add(3)
    assert bst.get(3) == 3
    bst.add(5)
    assert bst.get(5) == 5
    
def test_contains():
    bst = BinarySearchTree()
    assert bst.contains(3) == False
    bst.add(3)
    assert bst.contains(3) == True
    bst.add(5)
    assert bst.contains(5) == True
 
def test_remove():
    # Remove when node had no children
    bst = BinarySearchTree()
    assert bst.remove(2) == False
    bst.add(5)
    bst.add(2)
    bst.add(7)
    assert bst.remove(2) == True
    
    # Remove when node has one child
    bst2 = BinarySearchTree()
    assert bst2.remove(2) == False
    bst2.add(5)
    bst2.add(2)
    bst2.add(7)
    bst2.add(3)
    assert bst2.remove(2) == True
    
    # Remove when node has two children
    bst3 = BinarySearchTree()
    assert bst3.remove(2) == False
    bst3.add(5)
    bst3.add(2)
    bst3.add(7)
    bst3.add(3)
    bst3.add(1)
    assert bst3.remove(2) == True

def test_size():
    bst = BinarySearchTree()
    assert bst.remove(2) == False
    bst.add(5)
    bst.add(2)
    bst.add(7)
    bst.add(3)
    bst.add(1)
    assert bst.size() == 5
    bst.remove(2)
    assert bst.size() == 4

