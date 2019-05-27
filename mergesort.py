"""
merge sort implemented in python
"""
import numpy as np


def merge(A, p, q, r):
    m = q - p + 1
    n = r - q
    # copy of sorted subarrays
    L = A[p:q+1]
    R = A[q+1:]
    # add a sentinel value at the end of the array
    L.append(np.inf)
    R.append(np.inf)
    # merge the sorted subarrays
    i, j = 0, 0
    for k in range(p, r+1):
        if L[i] < R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2    # bisection the array
        # sort subarrays
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        # merge sorted subarrays
        merge(A, p, q, r)


if __name__ == '__main__':
    lst = [1, 3, 5, 2, 4, 6]
    print(lst)

    n = len(lst)
    merge_sort(lst, 0, n-1)
    print(lst)