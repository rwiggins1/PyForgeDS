from PyForgeDS.hashing.hashmap_chaining import hashMap

def test_insert():
    ht = hashMap(10)
    ht.put("A", 10)
    ht.put("a", 11)
    ht.put("b", 221)
    ht.put("4", 22)
    ht.put("2", 21)
    ht.put("1", 12)

    ht.display()

def test_size():
    ht = hashMap(10)
    ht.put("A", 10)
    ht.put("a", 11)
    ht.put("b", 221)
    ht.put("4", 22)
    ht.put("2", 21)
    ht.put("1", 12)

    assert ht.size() == 6

def test_is_empty():
    ht = hashMap(10)

    assert ht.isEmpty() == True

def test_contains():
    ht = hashMap()
    assert ht.contains(3) == False
    ht.put(3, 12)
    assert ht.contains(3) == True
    assert ht.contains(4) == False
