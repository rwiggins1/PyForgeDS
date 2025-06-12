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


test_insert()
