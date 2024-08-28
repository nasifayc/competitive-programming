class Node():
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
    
class Queue():
    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self, data):
        node = Node(data)
        if self.front == None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            node.prev = self.rear
            self.rear = node
    def dequeue(self):
        if self.front == None:
            return None
        temp = self.front
        data = temp.data
        self.front = temp.next
        return data


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(100)
    queue.enqueue(3)
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
