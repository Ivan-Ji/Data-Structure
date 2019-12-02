class Node(object):
    """define node"""
    def __init__(self, elem):
        self.elem = elem
        self.next = None
        self.prev = None


class DoubleLinkList(object):
    """双向链表"""
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        """链表是否为空"""
        return self.__head is None

    def length(self):
        """链表长度"""
        current = self.__head    # current游标移动遍历节点
        count = 0  # 记录数量
        while current is not None:
            count += 1
            current = current.next
        return count

    def travel(self):
        """遍历链表"""
        current = self.__head  # current游标移动遍历节点
        while current is not None:
            print(current.elem, end=' ')
            current = current.next

    def add(self, item):    # 头插法
        """头部添加元素"""
        node = Node(item)
        node.next = self.__head
        self.__head = node
        node.next.prev = node

    def append(self, item):     # 尾插法
        """尾部添加元素"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            current = self.__head
            while current.next is not None:
                current = current.next
            current.next = node
            node.prev = current

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
            current = self.__head
            count = 0  # 记录数量
            while count < pos:
                count += 1
                current = current.next
            node = Node(item)
            node.next = current
            node.prev = current.prev
            current.prev = node
            node.prev.next = node

    def remove(self, item):
        """删除元素"""
        current = self.__head
        while current is not None:
            if current.elem == item:
                # 先判断此节点是否是头节点，如果是头节点(pre==None)
                if current == self.__head:
                    self.__head = current.next
                    if current.next:    # 判断链表是否只有一个节点
                        current.next.prev = None
                else:
                    current.prev.next = current.next
                    if current.next:
                        current.next.prev = current.prev
                break
            else:
                current = current.next

    def search(self, item):
        """查找结点是否存在"""
        current = self.__head  # current游标移动遍历节点
        while current is not None:
            if current.elem == item:
                return True
            else:
                current = current.next
        return False


if __name__ == '__main__':
    ll = DoubleLinkList()
    print(ll.is_empty())
    ll.append(1)
    print(ll.length())
    ll.append(2)
    ll.add(8)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    print(ll.length())
    print(ll.travel())
    ll.insert(-1, 9)
    ll.insert(3, 100)
    ll.insert(10, 200)
    print(ll.travel())
    ll.remove(100)
    ll.remove(9)
    ll.remove(200)
    print(ll.travel())
