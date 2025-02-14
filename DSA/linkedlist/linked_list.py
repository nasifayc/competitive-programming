class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0
        
    

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        node = self.head
        for i in range(index):
            node = node.next
        return node.val

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head
        self.head = node
        self.size += 1
        

    def addAtTail(self, val: int) -> None:

        newNode = Node(val)
        
        if not self.head:
            self.head = newNode
            self.size += 1
            return

        node = self.head
        while node.next:
            node = node.next
        node.next = newNode
        self.size += 1
        

    def addAtIndex(self, index: int, val: int) -> None:

        if index < 0 or index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
            return

        newNode = Node(val)
        node = self.head
        for i in range(index-1):
            node = node.next
        newNode.next = node.next
        node.next = newNode
        self.size += 1

        

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return
        node = self.head
        for i in range(index-1):
            node = node.next
        temp = node.next
        node.next = temp.next
        self.size -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)