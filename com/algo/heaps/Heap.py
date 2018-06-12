class Heap:
    __slots__ = ['arr','size','capacity']
    def __init__(self,capacity):

        self.capacity = capacity
        self.arr=[None]*self.capacity
        self.size=0

    def insert(self,element):
        if(self.size>=self.capacity):
            print('Heap is full')
        else:
         self.arr[self.size]=element
         self.heapify_up()
         print(*self.arr, sep='\t')
         self.size=self.size+1

    def heapify_up(self):
        element=self.arr[self.size]
        index=self.size
        parent=(index-1)//2

        while(index>0 and self.arr[parent]<element):
            self.arr[index]=self.arr[parent]
            index=parent
            parent=(parent-1)//2

        self.arr[index]=element

    def delete(self):
        if(self.size==0):
            print('heap is empty')
        else:
            deleted_element=self.arr[0]
            self.arr[0]=self.arr[self.size-1]
            del self.arr[self.size-1]
            self.size=self.size-1
            self.heapify_down(0)
            print(*self.arr,sep='\t')
            return deleted_element


    def heapify_down(self,pos):
        element=self.arr[pos]
        index=0
        while(index<self.size//2):

            large_child_index=0
            left_child_index=2*index+1
            right_child_index=left_child_index+1
            if(left_child_index<self.size and self.arr[left_child_index]<self.arr[right_child_index]):
                large_child_index=right_child_index
            else:
                large_child_index=left_child_index

            if self.arr[large_child_index] < element:
                break
            else:
                self.arr[index]=self.arr[large_child_index]
                index=large_child_index

        self.arr[index]=element

    def print_heap(self):
        if(self.size==0):
            print('Heap is empty')
        else:
            print(*self.arr,sep='\t')




















if __name__=='__main__':
    heap =Heap(10)

    heap.insert(4)
    heap.insert(7)
    heap.insert(10)
    heap.insert(1)
    heap.insert(18)
    heap.insert(9)
    print('Deleted item = ',heap.delete())
