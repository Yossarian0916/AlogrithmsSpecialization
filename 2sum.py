"""
variant of 2-SUM problem
compute the number of target values t in the interval [-10000,10000],
such that there are distinct numbers x,y in the input file that satisfy x+y=t.

solution: modified binary search ( O(nclog(n)) ) works better than using 
          hash-table ( O(nm) ), because m is much larger than log2(n), where n 
          is the number of integers, m is the size of t (sum of x and y) range
"""


def count_sum_values(array, lower_bound, upper_bound):
    sum_values = list()
    low, high = 0, len(array) - 1
    while low < high:
        if array[low] + array[high] < lower_bound:
            low += 1
        elif array[low] + array[high] > upper_bound:
            high -= 1
        elif array[low] == array[high]:
            break
        else:
            sum = array[low] + array[high]
            low_idx = low
            while sum <= upper_bound:
                sum_values.append(sum)
                low_idx += 1
                if low_idx == high:
                    break
                sum = array[low_idx] + array[high]
            high -= 1
    return set(sum_values)


if __name__ == '__main__':
    array = list()
    with open('2sum.txt', 'r') as fd:
        for line in fd:
            array.append(int(line))

    res = count_sum_values(sorted(array), -10000, 10000)
    print(len(res))  # 427
