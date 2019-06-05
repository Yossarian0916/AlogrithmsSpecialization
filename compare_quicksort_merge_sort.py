from quicksort import quick_sort
from mergesort import merge_sort
from mergeSort import mergeSort
import timeit
import random


lst_duplicates = random.choices(range(100), k=10000)
lst_no_duplicates = random.sample(range(10000), k=10000)

t_quicksort = timeit.timeit(
    'quick_sort(lst_duplicates, 0, len(lst_duplicates)-1)', number=1, globals=globals())
t_mergesort = timeit.timeit(
    'merge_sort(lst_duplicates, 0, len(lst_duplicates)-1)', number=1, globals=globals())
t_mergeSort = timeit.timeit(
    'mergeSort(lst_duplicates)', number=1, globals=globals())
print('test array with duplicated elemntes')
print('quick_sort: ', t_quicksort)
print('merge_sort: ', t_mergesort)
print('mergeSort:  ', t_mergeSort)

t_quicksort = timeit.timeit(
    'quick_sort(lst_no_duplicates, 0, len(lst_no_duplicates)-1)', number=1, globals=globals())
t_mergesort = timeit.timeit(
    'merge_sort(lst_no_duplicates, 0, len(lst_no_duplicates)-1)', number=1, globals=globals())
t_mergeSort = timeit.timeit(
    'mergeSort(lst_no_duplicates)', number=1, globals=globals())
print('test array with NO duplicated elements')
print('quick_sort: ', t_quicksort)
print('merge_sort: ', t_mergesort)
print('mergeSort:  ', t_mergeSort)
