def quick_sort(data, start, end):
    """快速排序"""
    if start >= end:
        return
    mid_value = data[start]
    low = start
    high = end
    # 代码思路
    # if data[high] < mid_value:
    #     data[low] = data[high]
    #     low += 1
    # elif data[high] > mid_value:
    #     high -= 1
    # if data[low] > mid_value:
    #     data[high] = data[high]
    #     high -= 1
    # elif data[low] < mid_value:
    #     low += 1
    while low < high:
        while low < high and data[high] >= mid_value:       # 包含等于的情况，将相等的元素放到一边去，该例子中放到了右边
            high -= 1
        data[low] = data[high]
        while low < high and data[low] < mid_value:
            low += 1
        data[high] = data[low]
    # 循环退出时，low == high
    data[low] = mid_value

    # 对low左边的列表进行排序，对high右边的列表进行排序，进行递归
    quick_sort(data, start, low-1)
    quick_sort(data, low+1, end)


if __name__ == '__main__':
    data = [100, 1, 2, 3, 4, 50, 5, 6, 7, 8, 9]
    print(data)
    quick_sort(data, 0, len(data)-1)
    print(data)
    # 最优时间复杂度为O(n*logn)，最坏时间复杂度为O(n*n)
