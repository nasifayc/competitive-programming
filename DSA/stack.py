class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack():
    def __init__(self):
        self.head = None
    def push(self, data):
        node  = Node(data)
        if self.head is None:
            self.head = node
            return
        node.next = self.head
        self.head = node
    def peek(self):
        if self.head is None:
            return 'List is empty'
        return self.head.data
    def pop(self):
        if self.head is None:
            return 'List is empty'
        temp = self.head
        data = temp.data
        self.head = temp.next
        temp = None
        return data
    def isEmpty(self)-> bool:
        return True if self.head is None else False
    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count
    def display(self):
       if self.head is None: 
           print('Stack is empty')
       current_node = self.head
       while current_node:
          print(current_node.data, end="->")
          current_node = current_node.next
        
    


if __name__ == '__main__':
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print(stack.size())
    print(stack.pop())
    print(stack.size())
    print(stack.pop())
    print(stack.size())
    print(stack.pop())
    print(stack.size())
    print(stack.pop())
