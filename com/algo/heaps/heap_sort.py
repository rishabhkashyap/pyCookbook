class HeapSort:
    def __init__(self, arr):
        self.arr = arr
        self.size = len(arr)

    def __swap(self, i, j):
        temp = self.arr[i]
        self.arr[i] = self.arr[j]
        self.arr[j] = temp

    def __get_left_index(self, i):
        return 2 * i + 1

    def __get_right_index(self, i):
        return 2 * i + 2

    def heapifyDown(self, i):
        large_index = i
        left_index = self.__get_left_index(i)
        right_index = self.__get_right_index(i)
        if (left_index < self.size and self.arr[left_index] > self.arr[large_index]):
            large_index = left_index
        if (right_index < self.size and self.arr[right_index] > self.arr[large_index]):
            large_index = right_index

        if (large_index != i):
            self.__swap(i, large_index)
            self.heapifyDown(large_index)

    def sort(self):
        j = self.size - 1
        while (j >= 0):
            self.heapifyDown(j)
            j -= 1

        while (self.size > 0):
            temp = self.arr[0]
            self.arr[0] = self.arr[self.size - 1]
            self.arr[self.size - 1] = temp
            self.size -= 1
            self.heapifyDown(0)

    def print_array(self):
        print(*self.arr)


if __name__ == "__main__":
    arr = [5, 4, 3, 2, 1]
    heap_sort = HeapSort(arr)
    heap_sort.sort()
    heap_sort.print_array()
