from PyForgeDS.lists.LinkBasedList import LinkBasedList

def test_add():
    lbl = LinkBasedList()
    assert lbl.num_elements == 0
    lbl.add(0, 10)
    lbl.add(1, 20)
    assert lbl.getFront().getData() == 10
    assert lbl.getRear().getData() == 20
    lbl.add(0, 1)
    assert lbl.getFront().getData() == 1
    assert lbl.getFront().getNext().getData() == 10
    assert lbl.getRear().getData() == 20

