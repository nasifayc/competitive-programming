class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return True if self.head is None else False
    def push(self,data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
    def peek(self):
        return self.head.data if self.head else None
    def pop(self):
        if self.head is None:
            return None
        else:
            temp = self.head
            data = temp.data
            self.head = temp.next
            return data
    def clearDigits(self, s: str) -> str:
        for char in s:
            if char.isalpha():
                self.push(char)
            elif char.isdigit():
                self.pop()
        result = ''

        while not self.isEmpty():
            result += self.pop()
        return result[::-1]

        