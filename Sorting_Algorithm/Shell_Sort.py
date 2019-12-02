# 按照步长进行排序
def shell_sort(data):
    length = len(data)
    gap = length//2
    while gap > 0:
        for i in range(gap, length):        # 插入排序
            while i > 0:
                if data[i] < data[i-gap]:
                    data[i], data[i-gap] = data[i-gap], data[i]
                    i -= gap
                else:
                    break
        gap //= 2


if __name__ == '__main__':
    data = [100, 1, 2, 3, 4, 50, 5, 6, 7, 8, 9]
    shell_sort(data)
    print(data)
    # 最坏时间复杂度为O(n*n),稳定性为不稳定的
