from typing import List


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

    def calPoints(self, operations: List[str]) -> int:
        for s in operations:
            if s == '+':
                x = self.pop()
                y = self.pop()
                t = x + y
                self.push(y)
                self.push(x)
                self.push(x + y)
            elif s == 'D':
                x = self.peek()
                self.push(x*2)
            elif s == 'C':
                self.pop()
            else:
                self.push(int(s))
        total = 0
        current = self.head
        while not self.isEmpty():
            total += self.pop()
            
        return total
    

if __name__ == '__main__':
    solution = Solution()
    print(solution.calPoints(["5","2","C","D","+"])) 