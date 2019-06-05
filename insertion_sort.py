# insertion sort
def insertion_sort(array):
    for i in range(1, len(array)):
        # insert key into sorted subarray
        card = array[i]
        j = i-1
        while j >= 0 and array[j] > card:
            array[j+1] = array[j]
            j = j-1
        array[j+1] = card


if __name__ == '__main__':
    lst = [8, 7, 3, 6, 3, 2]
    insertion_sort(lst)
    print(lst)
