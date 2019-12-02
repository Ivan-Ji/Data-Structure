# coding:utf-8


class Node(object):
    """define node"""
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleCycleLinkList(object):
    """单向循环链表"""
    def __init__(self, node=None):
        self.__head = node
        if node:
            node.next = node

    def is_empty(self):
        """链表是否为空"""
        return self.__head is None

    def length(self):
        """链表长度"""
        if self.is_empty():
            return 0
        current = self.__head    # current游标移动遍历节点
        count = 1  # 记录数量
        while current.next != self.__head:
            count += 1
            current = current.next
        return count

    def travel(self):
        """遍历链表"""
        if self.is_empty():
            return
        current = self.__head  # current游标移动遍历节点
        while current.next != self.__head:
            print(current.elem, end=' ')
            current = current.next
        print(current.elem)     # 退出循环后，打印尾节点的元素

    def add(self, item):    # 头插法
        """头部添加元素"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
            return
        current = self.__head
        while current.next != self.__head:
            current = current.next
        # 退出循环后，询问尾节点
        node.next = self.__head
        self.__head = node
        # current.next = node
        current.next = self.__head

    def append(self, item):     # 尾插法
        """尾部添加元素"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            current = self.__head
            while current.next != self.__head:
                current = current.next
            # node.next = current.next
            # current.next = node
            # 上面的代码和下面的代码都可用
            current.next = node
            node.next = self.__head

    def insert(self, pos, item):
        """指定位置添加元素
        :param pos: 从0开始
        :param item:
        """
        if pos <= 0:
            self.add(item)
        elif pos > self.length() - 1:
            self.append(item)
        else:
            pre = self.__head
            count = 0  # 记录数量
            while count < (pos - 1):
                count += 1
                pre = pre.next
            node = Node(item)
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        """删除元素"""
        if self.is_empty():
            return

        current = self.__head
        pre = None
        while current.next != self.__head:
            if current.elem == item:
                # 先判断此节点是否是头节点，如果是头节点(pre==None)
                if current == self.__head:      # 头节点的情况，找尾节点
                    rear = self.__head      # 尾节点命名为rear
                    while rear.next != self.__head:
                        rear = rear.next
                    self.__head = current.next
                    rear.next = self.__head
                else:
                    pre.next = current.next
                return
            else:
                pre = current
                current = current.next
        # 退出循环，current指向尾节点
        if current.elem == item:
            if current == self.__head:
                self.__head = None
            else:
                pre.next = current.next

    def search(self, item):
        """查找结点是否存在"""
        if self.is_empty():
            return False
        current = self.__head  # current游标移动遍历节点
        while current.next != self.__head:
            if current.elem == item:
                return True
            else:
                current = current.next
        if current.elem == item:
            return True
        return False


if __name__ == '__main__':
    sll = SingleCycleLinkList()
    print(sll.is_empty())
    sll.append(1)
    print(sll.length())
    sll.append(2)
    sll.add(8)
    sll.append(3)
    sll.append(4)
    sll.append(5)
    sll.append(6)
    print(sll.length())
    print(sll.travel())
    sll.insert(-1, 9)
    sll.insert(3, 100)
    sll.insert(10, 200)
    print(sll.travel())
    sll.remove(100)
    sll.remove(9)
    sll.remove(200)
    print(sll.travel())
