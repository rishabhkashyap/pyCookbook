class QuickSort:
    __slots__ = ['__arr', 'size']

    def __init__(self, arr):
        self.__arr = arr
        self.size = len(arr)

    def sort(self, low, high):
        i = low
        j = high
        mid = self.__arr[low + (high - low) // 2]
        while (i <= j):
            while (self.__arr[i] < mid):
                i += 1
            while (self.__arr[j] > mid):
                j -= 1
            if (i <= j):
                temp = self.__arr[i]
                self.__arr[i] = self.__arr[j]
                self.__arr[j] = temp
                i += 1
                j -= 1

        if (low < j):
            self.sort(low, j)

        if (high > i):
            self.sort(i, high)

    def display(self):
        print(*self.__arr)
        print('\n')


if __name__ == '__main__':
    arr = [10, 7, 8, 9, 1, 5]
    quick_sort = QuickSort(arr)
    print('Array before sorting')
    quick_sort.display()
    quick_sort.sort(0, len(arr) - 1)
    print('Array after sorting')
    quick_sort.display()
