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

def heapify( n , arr , idx):
    
    left = (2 * idx) + 1
    right = (2 * idx) + 2
    largest = idx

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    if largest != idx:
        arr[idx], arr[largest] = arr[largest], arr[idx]
        heapify(n ,arr, largest)

def heap_sort(arr):
    n = len(arr)
    print("original array:",arr)
    for idx in range((n // 2) - 1 , -1 , -1):
        heapify(n , arr, idx )


    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]

        heapify(i, arr, 0)
    return arr


# Example usage:

if __name__ == "__main__":
    heap = MinHeap()

    data = [2 , 30 , 20, 12, 9]
    for i in data :
        heap.insert(i)

    # delete elements
    heap.delete(30)
    heap.delete(12)

    # check that heap is valid or not
    print(heap.is_valid_heap())

    # print the heap
    print(heap.heap)

    # heap sort
    arr = [ 9 ,3 ,40 ,8 ,5]
    print(heap_sort(arr))