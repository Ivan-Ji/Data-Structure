def insert_sort(data):
    """插入排序
    :param data:
    """
    length = len(data)
    for i in range(1, length):
        while i > 0:
            if data[i] < data[i - 1]:
                data[i], data[i-1] = data[i-1], data[i]
                i -= 1
            else:
                break


if __name__ == '__main__':
    # 将list分为两个部分，第一部分为已排好的数据，第二部分为未排序的数据，
    # 将第二部分的第一个元素插入到第一部分已经排好顺序的序列中
    data = [100, 1, 2, 3, 4, 50, 5, 6, 7, 8, 9]
    insert_sort(data)
    print(data)
    # 最坏时间复杂度为O(n*n),最优时间复杂度为O(n),稳定性是稳定的
