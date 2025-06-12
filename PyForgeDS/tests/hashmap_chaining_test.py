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

test_insert()
