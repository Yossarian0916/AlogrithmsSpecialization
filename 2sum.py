def count_sum_values(array):
    sum_values = set()
    low = 0
    high = len(array) - 1
    while low < high:
        if array[low] + array[high] < -10000:
            low += 1
        elif array[low] + array[high] > 10000:
            high -= 1
        else:
            sum = array[low] + array[high]
            while -10000 < sum < 10000:
                sum_values.add(sum)
                low += 1
                if low == high:
                    break
                sum = array[low] + array[high]
            high -= 1
    return sum_values


if __name__ == '__main__':
    array = list()
    with open('2sum.txt', 'r') as fd:
        for line in fd:
            array.append(int(line))

    res = count_sum_values(sorted(array))
    print(res)
    print(len(res))
