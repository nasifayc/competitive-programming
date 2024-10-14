class Pair:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:

    def __init__(self):
        self.size = 10
        self.hash = [None for _ in range(self.size)]
        
    def hashValue(self,key)->int:
        return key % self.size

    def put(self, key: int, value: int) -> None:
        i = self.hashValue(key)
        pair = Pair(key,value)

        if not self.hash[i]:
            self.hash[i] = pair
        else:
            cur = self.hash[i]
            while cur:
                if cur.key == key:
                    cur.val = value
                    return
                if not cur.next:
                    break
                cur = cur.next
            cur.next = pair
        
        

    def get(self, key: int) -> int:
        i = self.hashValue(key)
        if not self.hash[i]:
            return -1
        elif self.hash[i].key == key:
            return self.hash[i].val
        else:
            curr = self.hash[i].next
            while curr:
                if curr.key == key:
                    return curr.val
                curr = curr.next
            return -1

        

    def remove(self, key: int) -> None:
        i = self.hashValue(key)
        if not self.hash[i]:
            return
        elif self.hash[i].key == key:
            self.hash[i] = self.hash[i].next
        else:
            curr = self.hash[i]
            while curr.next:
                if curr.next.key == key:
                    curr.next = curr.next.next
                    return
                curr = curr.next
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)