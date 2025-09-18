from PyForgeDS.queues.LinkBasedQueue import LinkBasedQueue

def test_enqueue():
    lbq = LinkBasedQueue()
    lbq.enqueue(1)
    lbq.enqueue(2)
    lbq.enqueue(3)
    lbq.enqueue(4)
    assert(lbq.getFront().getData() == 1)
    assert(lbq.getRear().getData() == 4)

def test_dequeue():
    lbq = LinkBasedQueue()
    lbq.enqueue(1)
    lbq.enqueue(2)
    lbq.enqueue(3)
    lbq.enqueue(4)
    assert(lbq.dequeue() == 1)

