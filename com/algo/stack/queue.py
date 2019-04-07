class Queue:
    __slots__ = ['__queue', '__size','__rear']

    def __init__(self, capacity):
        self.__queue = [None]*capacity
        self.__size = 0;
        self.__rear=-1

    def enqueue(self,element):
        if(self.__size==len(self.__queue)):
            print('Queue is full')
        else:
            self.__rear+=1
            self.__queue[self.__rear]=element
            self.__size+=1

    def dequeue(self):
        if(self.__size==0):
            print('Queue is emplty')
        else:
            return self.__queue.pop(0)


    def peek(self):
        if(self.__size==0):
            return None
        else:
            return self.__queue[0]

    def display_queue(self):
        print(self.__queue)




if __name__=='__main__':
    queue=Queue(5)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(3)
    # queue.enqueue(3)
    #queue.enqueue(3)

    queue.display_queue()
    print('\n')
    print(queue.dequeue())
    print(queue.dequeue())
    print('\n')
    queue.display_queue()


