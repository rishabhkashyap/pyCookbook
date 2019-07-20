class Node:
    __slots__ = ['__data', '__next']

    def __init__(self, data=None, node=None):
        self.__data = data
        self.__next = data

    def get_data(self):
        return self.__data

    def get_next(self):
        return self.__next

    def set_data(self, data):
        self.__data = data

    def set_next(self, next):
        self.__next
