class Stack:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__size = 0
        self.__queue = []

    def push(self, element):
        if (self.__size == self.__capacity):
            print("Stack is full")
            return
        self.__queue.append(element)
        self.__size += 1

    def pop(self):
        if (self.__size == 0):
            print("Stack is full")
            return
        count = self.__size
        while (count > 1):
            self.__queue.append(self.__queue.pop(0))
            count -= 1

        element = self.__queue.pop(0)
        self.__size -= 1
        return element


if __name__ == "__main__":
    stack = Stack(5)
    stack = Stack(5)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    print(f"Poped element = {stack.pop()}")
