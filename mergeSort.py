def mergeSort(array):
    if len(array) == 1:
        return array
    else:
        mid = len(array) // 2
        left = mergeSort(array[:mid])
        right = mergeSort(array[mid:])
    return merge(left, right)


def merge(left, right):
    res = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        elif left[i] >= right[j]:
            res.append(right[j])
            j += 1

    res += left[i:]
    res += right[j:]
    return res
