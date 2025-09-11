from PyForgeDS.lists.LinkBasedList import LinkBasedList
from PyForgeDS.base.LLNode import LLNode

def test_node():
    node = LLNode(12)
    assert node.getData() == 12
    node.setData(13)
    assert node.getData() == 13

def test_add():
    lbl = LinkBasedList()
    assert lbl.num_elements == 0
    lbl.add(0, 10)
    lbl.add(1, 20)
    assert lbl.getFront().getData() == 10
    assert lbl.getRear().getData() == 20
    lbl.add(0, 1)
    assert lbl.getFront().getData() == 1
    print(lbl)

