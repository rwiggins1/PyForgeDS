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

