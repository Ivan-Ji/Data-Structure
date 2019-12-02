def merge_sort(data):
    """归并算法"""
    # 使用递归
    length = len(data)
    if length <= 1:
        return data
    mid = length//2
    # 利用left,right进行递归，形成有序的列表
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])

    # 将left, right进行合并排序
    left_pointer, right_pointer = 0, 0
    result = []
    while left_pointer < len(left) and right_pointer < len(right):
        if left[left_pointer] <= right[right_pointer]:
            result.append(left[left_pointer])
            left_pointer += 1
        else:
            result.append(right[right_pointer])
            right_pointer += 1
    result += left[left_pointer:]
    result += right[right_pointer:]
    return result


if __name__ == '__main__':
    data = [100, 1, 2, 3, 4, 50, 5, 6, 7, 8, 9]
    sorted_result = merge_sort(data)
    print(sorted_result)
    # 最坏时间复杂度O(n*logn)
