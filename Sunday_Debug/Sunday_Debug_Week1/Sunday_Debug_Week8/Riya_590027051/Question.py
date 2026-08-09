class MaxHeap:
    def __init__(self):
        self.heap = []

    # Insert an element and bubble it up
    def insert(self, value):
        self.heap.append(value)

        index = len(self.heap) - 1

        while index > 0:
            parent = (index - 1) // 2

            if self.heap[index] > self.heap[parent]:
                self.heap[index], self.heap[parent] = (
                    self.heap[parent],
                    self.heap[index]
                )
                index = parent
            else:
                break

    # Extract the maximum element
    def extract_max(self):
        if not self.heap:
            return None

        maximum = self.heap[0]

        # Move last element to the root
        last = self.heap.pop()

        if self.heap:
            self.heap[0] = last

            # Bubble down
            index = 0

            while True:
                left = 2 * index + 1
                right = 2 * index + 2
                largest = index

                if (
                    left < len(self.heap)
                    and self.heap[left] > self.heap[largest]
                ):
                    largest = left

                if (
                    right < len(self.heap)
                    and self.heap[right] > self.heap[largest]
                ):
                    largest = right

                if largest == index:
                    break

                self.heap[index], self.heap[largest] = (
                    self.heap[largest],
                    self.heap[index]
                )

                index = largest

        return maximum

    # Display heap
    def display(self):
        print("Heap:", *self.heap)


# Main program
heap = MaxHeap()

heap.insert(60)
heap.insert(50)
heap.insert(40)
heap.insert(10)
heap.insert(25)

heap.display()

extracted = heap.extract_max()
print("Extracted:", extracted)

heap.display()