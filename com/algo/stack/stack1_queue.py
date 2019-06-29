


class Queue:
    def __init__(self, size):
        self.__stack = []
        self.__size = size

    def insert_element(self, element):
         if(len(self.__stack)==0):
             self.__stack.append(element)
         else:
             temp=self.__stack.pop()
             self.insert_element(element)
             self.__stack.append(temp)

    def enqueue(self, element):
        if (len(self.__stack) == self.__size):
            print("Queue is full")
        elif(len(self.__stack)==0):
            self.__stack.append(element)
        else:
            self.insert_element(element)

    def dequeue(self):
        if(len(self.__stack)==0):
            print("Queue is empty")
            return
        return self.__stack.pop()



if __name__=="__main__":
    queue=Queue(5)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)

    print(f"Dequed element = {queue.dequeue()}")
    print(f"Dequed element = {queue.dequeue()}")
    print(f"Dequed element = {queue.dequeue()}")