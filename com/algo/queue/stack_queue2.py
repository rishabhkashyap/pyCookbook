class Stack:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__size = 0
        self.__queue1 = []
        self.__queue2 = []

    def push(self, element):
        if (self.__size == self.__capacity):
            print("Stack full")
            return
        if (len(self.__queue1) == 0):
            self.__queue1.append(element)
            self.__size += 1
        else:

            while len(self.__queue1) != 0:
                self.__queue2.append(self.__queue1.pop(0))

            self.__queue1.append(element)
            self.__size += 1

            while len(self.__queue2) != 0:
                self.__queue1.append(self.__queue2.pop(0))

    def pop(self):
        if (self.__size == 0):
            print("Stack is empty")
            return
        element = self.__queue1.pop(0)
        self.__size -= 1
        return element

    def display(self):
        print(*self.__queue1)


if __name__ == "__main__":
    stack = Stack(5)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.display()
    print(f"Poped element = {stack.pop()}")
    stack.display()
