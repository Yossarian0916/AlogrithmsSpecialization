def binary(array, val):
    # boundary check, when the val is not in array
    if val < array[0] or val > array[-1]:
        return False
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = low + (high-low) // 2
        if val == array[mid]:
            return mid
        elif val < array[mid]:
            high = mid
        elif val > array[mid]:
            low = mid
    return False


def binary_recursive(array, val):
    # boundary check, when the val is not in array
    if val < array[0] or val > array[-1]:
        return False

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
    res = binary_recursive(lst, 13)
    print(res)
