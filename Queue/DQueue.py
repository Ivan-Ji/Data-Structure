class DQueue(object):
    """双端队列"""

    def __init__(self):
        self.__list = []

    def add_front(self, item):
        """头部添加元素"""
        self.__list.insert(0, item)

    def add_rear(self, item):
        """尾部添加元素"""
        self.__list.append(item)

    def pop_front(self):
        """头部出队"""
        return self.__list.pop(0)

    def pop_rear(self):
        """尾部出队"""
        return self.__list.pop()

    def is_empty(self):
        """判空"""
        return self.__list == []

    def size(self):
        """队列的长度"""
        return len(self.__list)


if __name__ == '__main__':
    q = DQueue()



