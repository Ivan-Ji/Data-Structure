def bubble_sort(data_list):
    """冒泡排序
    :param data_list: list
    :return: list
    """
    length = len(data_list)
    for i in range(length-1):
        count = 0
        for j in range(length - i - 1):
            if data_list[j] > data_list[j + 1]:
                data_list[j], data_list[j + 1] = data_list[j + 1], data_list[j]
                count += 1
        if count == 0:
            break
    return data_list


if __name__ == '__main__':
    data = [100, 1, 2, 3, 4, 50, 5, 6, 7, 8, 9]
    data = bubble_sort(data)
    print(data)
    # 冒泡排序算法稳定
    # 该方法最优时间复杂度为O(n),最坏时间复杂度为O(n*n),利用count进行判断是否交换过位置
