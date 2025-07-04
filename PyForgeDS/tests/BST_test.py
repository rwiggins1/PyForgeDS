from warnings import warn
from PyForgeDS.trees.BinarySearchTree import BinarySearchTree

def test_isEmpty():
    bst = BinarySearchTree()
    assert bst.isEmpty() == True

def test_add():
    bst = BinarySearchTree()
    bst.add(12)
    assert bst.root.info == 12
    bst.add(10)
    assert bst.root.left.info == 10
    bst.add(94)
    assert bst.root.right.info == 94

def test_min_max():
    bst = BinarySearchTree()
    bst.add(12)
    assert bst.root.info == 12
    bst.add(10)
    assert bst.root.left.info == 10
    bst.add(94)
    assert bst.root.right.info == 94
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
    
