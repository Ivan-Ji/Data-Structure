def select_sort(data):
    """选择排序
    :param data: list
    :return: list
    """
    length = len(data)
    for i in range(length - 1):
        min_index = i
        for j in range(i+1, length, 1):
            if data[j] < data[min_index]:
                min_index = j
        data[i], data[min_index] = data[min_index], data[i]
    return data


if __name__ == '__main__':
    # 将list分为两个部分，第一部分为已排好的数据，第二部分为未排序的数据，将第二部分最小的元素放到第一部分的最后
    # 但遇到相同元素时该排序算法不稳定
    data = [100, 1, 2, 3, 4, 50, 5, 6, 7, 8, 9]
    sorted_data = select_sort(data)
    print(sorted_data)
    # 时间复杂度为O(n*n)
