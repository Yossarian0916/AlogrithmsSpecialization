"""implementation of bubble sort"""
def bubble_sort(array):
    """sort in incremental order"""
    n = len(array)
    for i in range(n):
        for j in range(n - i -1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
            print(array)


def short_bubble_sort(lst):
    """sort in incremental order, stop early if there is no exchange needed"""
    array = lst.copy()
    n = len(array)
    exchange = True
    for i in range(n):
        if exchange:
            exchange = False
            for j in range(n - i -1):
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
                    exchange = True
        else:
            return array
    
    return array


if __name__ == '__main__':
    lst = [1, 3, 5, 2, 4, 6]
    sorted_lst = short_bubble_sort(lst)
    print(lst)