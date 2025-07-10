from PyForgeDS.lists.LinkBasedList import LinkBasedList

def test_add():
    lbl = LinkBasedList()
    assert lbl.num_elements == 0
    lbl.add(0, 10)
    lbl.add(1, 20)
    print(lbl.front.data, lbl.rear.data)
    lbl.add(0, 1)
    print(lbl.front.data, lbl.front.next.data, lbl.rear.data)
    print(lbl)

