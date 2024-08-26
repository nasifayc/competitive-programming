class Node():
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None


class HashTable():
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * self.capacity
    def _hash(self,key):
        return hash(key) % self.capacity
    def insert(self,key,value):
        index = self._hash(key)
        node = Node(key,value)
        if(self.table[index] == None):
            self.table[index] = node
            self.size += 1
        else:
            current = self.table[index]
            while current:
                if current.key == key:
                    current.value = value
                    return
                current = current.next
            node.next = self.table[index]
            self.table[index] = node
            self.size += 1

    def search(self, key):
        index = self._hash(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return 'Invalid Key'
    
    def remove(self,key):
        index = self._hash(key)
        previous = None
        current = self.table[index]

        while current:
            if current.key == key:
                if previous:
                    previous.next = current.next
                else:
                    self.table[index] = current.next
                self.size -= 1
                print(f"key : {key} , value : {current.value} removed")
                return
            previous = current
            current = current.next
        print(f"{key} not found")

    def __str__(self):
        elements = []
        for i in range(self.capacity):
            current = self.table[i]
            while current:
                elements.append((current.key, current.value))
                current = current.next
            
        return str(elements)
    
        

    
if __name__ == "__main__":
    hashtable = HashTable(1)

    print('\n-------------------insert ------------------------')

    hashtable.insert('john', 20)
    hashtable.insert('david', 30)
    hashtable.insert('olivia', 40)
    hashtable.insert('johns', 50)
    hashtable.insert('davids', 60)
    hashtable.insert('olivias', 70)

    print(hashtable.__str__())

    print('\n-------------------searched results ------------------------')


    
    print(hashtable.search('john'))
    print(hashtable.search('david')) 
    print(hashtable.search('olivia')) 
    print(hashtable.search('johns')) 
    print(hashtable.search('davids'))
    print(hashtable.search('olivias'))

    print('\n-------------------delete ------------------------')
    hashtable.remove('johns')
    hashtable.remove('davids')
    hashtable.remove('davidcsrdes')

    print(hashtable.__str__())

