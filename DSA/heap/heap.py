class Heap:
    def __init__(self):
        self.heap = [0]

    def push(self,val):
        self.heap.append(val)
        
        i = len(self.heap) - 1

        # Percolate up
        while i > 1 and self.heap[i] < self.heap[i // 2]:
            self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i //= 2

    def pop(self):
        if len(self.heap) == 1:
            return None
        if len(self.heap) == 2:
            return self.heap.pop()
        
        res = self.heap[1]

        # Move last value to root
        self.heap[1] = self.heap.pop()
        i = 1

        # Percolate down
        while i * 2 < len(self.heap):
            if (i * 2 + 1 < len(self.heap)) and self.heap[i * 2 + 1] < self.heap[i * 2] and self.heap[i] > self.heap[i * 2 + 1]:
                # Swap right child
                self.heap[i], self.heap[i * 2 + 1] = self.heap[i * 2 + 1], self.heap[i]
                i = i * 2 + 1
            elif self.heap[i] > self.heap[i * 2]:
                # Swap left child
                self.heap[i], self.heap[i * 2] = self.heap[i * 2], self.heap[i]
                i = i * 2
            else:
                break
        
        return res
    
    def print(self):
        print("Heap:", self.heap[1:])  # Print the heap (excluding the 0 at index 0)
        copy = self.heap[:]
        result = []
        
        # Pop all elements without modifying the original heap
        while len(copy) > 1:
            # Temporarily use the pop logic on the copy
            temp_heap = Heap()
            temp_heap.heap = copy[:]
            result.append(temp_heap.pop())
            copy = temp_heap.heap
        
        print("Priority Queue:", result)
            

if __name__ == '__main__':
    heap = Heap()
    heap.push(5)
    heap.push(3)
    heap.push(1)
    heap.push(8)
    heap.push(2)
    heap.push(7)
    heap.print()
    
    # heapq is python built in function to impliment heap a.k.a priority queue