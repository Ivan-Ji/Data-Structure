# 二分查找是经过排序之后进行的操作,也叫做折半查找


def binary_search_recursion(data, item):
    """二分查找-使用递归"""
    length = len(data)
    if length > 0:
        mid = length//2
        if data[mid] == item:
            return True
        elif data[mid] < item:
            return binary_search_recursion(data[mid+1:], item)
        else:
            return binary_search_recursion(data[:mid], item)
    return False


def binary_search_loop(data, item):
    """二分查找-使用循环"""
    length = len(data)
    start = 0
    end = length - 1
    while start <= end:
        mid_index = (start + end) // 2
        if data[mid_index] == item:
            return True
        elif data[mid_index] > item:
            end = mid_index - 1
        else:
            start = mid_index + 1
    return False


if __name__ == '__main__':
    data = [100, 1, 2, 3, 4, 50, 5, 6, 7, 8, 9]
    print(binary_search_recursion(data, 66))
    print(binary_search_loop(data, 66))
    # 最坏时间复杂度为O(logn),最优时间复杂度为O(1)
