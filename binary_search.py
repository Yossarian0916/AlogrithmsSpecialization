def binary(array, val):
    low = 0
    high = len(array) - 1
    while low < high:
        mid = (low + high) // 2
        if val == array[mid]:
            return mid
        elif val < array[mid]:
            high = mid
        elif val > array[mid]:
            low = mid


def binary_recursive(array, val):
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]
    if val == array[mid]:
        return True
    elif array[mid] > val:
        return binary_recursive(left, val)
    elif array[mid] < val:
        return binary_recursive(right, val)
    else:
        return False


if __name__ == "__main__":
    lst = list(range(0, 12))
    res = binary_recursive(lst, 5)
    print(res)
