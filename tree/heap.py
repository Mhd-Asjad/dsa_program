class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self , data):
        self.heap.append(data)
        self.bubble_up(len(self.heap)-1)

    def bubble_up(self , idx):
        parent = (idx - 1) // 2
        while idx > 0 and self.heap[idx] < self.heap[parent]:
            self.heap[parent] , self.heap[idx] = self.heap[idx] , self.heap[parent]
            idx = parent 
            parent = (idx - 1) // 2

    def delete(self, value ):
        try :
            index = self.heap.index(value)
        
        except:
            raise ValueError(f"{value} not in heap")
        
        n = len(self.heap) - 1
        self.swap(index , n )
        min_value = self.heap.pop()
        return f"{min_value} deleted successfully....!"
        

    def bubble_down(self,idx):
        n = len(self.heap)
        smallest = idx

        while True:
            
            left = (2 * idx) + 1
            right = (2 * idx) + 2

            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left 

            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest != idx:
                self.swap(idx , smallest)
                idx = smallest
            else :
                break

    def swap(self, i , j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


    def is_valid_heap(self):
        n = len(self.heap)

        for idx in range((n // 2)):
            left = (2 * idx) + 1
            right = (2 * idx) + 2

            if left < n and self.heap[idx] > self.heap[left]:
                return False
            if right < n and self.heap[idx] > self.heap[right]:
                return False
        return True

data = [2 , 30 , 20, 12, 9]
heap = MinHeap()
for i in data :
    heap.insert(i)

# heap.delete(30)
# heap.delete(12)

print(heap.heap)
print(heap.is_valid_heap())