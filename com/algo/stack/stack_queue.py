class Queue:
    def __init__(self, size):
        self.__stack1 = []
        self.__stack2 = []
        self.__size = size

    def enqueue(self, element):
        if (len(self.__stack1) == self.__size):
            print("Queue is full")
        else:
            self.__stack1.append(element)

    def dequeue(self):
        if (len(self.__stack1) == 0 and len(self.__stack2)==0):
            print("Queue is empty")
        else:
            if (len(self.__stack2) != 0):
                return self.__stack2.pop()
            else:
                while (len(self.__stack1) != 0):
                    self.__stack2.append(self.__stack1.pop())
                return self.__stack2.pop()



if __name__=="__main__":
    queue=Queue(5)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)

    print(f"Dequed element = {queue.dequeue()}")
    print(f"Dequed element = {queue.dequeue()}")