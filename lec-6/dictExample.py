from typing import Any


class MyDict:
    def __init__(self):
        self.size = 8
        self.hashmap = [[] for _ in range(0, self.size)]
        print('self.hashmap {}'.format(self.hashmap))

    def custom_hash(self, key):
        print('hash of key {}'.format(hash(key)))
        indexed_key = hash(key) % (self.size -1)
        print('indexed key {}'.format(indexed_key))
        return indexed_key
    
    def insert_item(self, key, value):
        print('key: {}'.format(key))
        hash_key = self.custom_hash(key)
        print('hash_key: {}'.format(hash_key))
        key_exists = False
        bucket = self.hashmap[hash_key]
        print('bucket: {}'.format(bucket))
        for i, kv in enumerate(bucket):
            print('i and kv {} {}'.format(i,kv))
            k, v = kv
            if key == k:
                key_exists = True
                break
        if key_exists:
            bucket[i] = ((key, value))
        else:
            bucket.append((key, value))

    def get_item(self, key):
        hash_key = self.custom_hash(key)
        bucket = self.hashmap[hash_key]
        for kv in bucket:
            k, v = kv
            if key == k:
                return v
            else:
                raise KeyError("Key does not exists.")
    
    def __setitem__(self, key, value):
        return self.insert_item(key, value)
    
    def __getitem__(self, key):
        return self.get_item(key)

d = MyDict()
d.insert_item("key1","val1")
print(d.get_item('key1'))