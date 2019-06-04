from quicksort import quick_sort
from mergesort import merge_sort
import timeit
import random


lst_duplicates = random.choices(range(100), k=10000)
lst_no_duplicates = random.sample(range(10000), k=10000)

t_quicksort = timeit.timeit(
    'quick_sort(lst_duplicates, 0, len(lst_duplicates)-1)', number=1, globals=globals())
t_mergesort = timeit.timeit(
    'merge_sort(lst_duplicates, 0, len(lst_duplicates)-1)', number=1, globals=globals())
print('test array with duplicated elemntes')
print('quicksort: ', t_quicksort)
print('mergesort: ', t_mergesort)

t_quicksort = timeit.timeit(
    'quick_sort(lst_no_duplicates, 0, len(lst_no_duplicates)-1)', number=1, globals=globals())
t_mergesort = timeit.timeit(
    'merge_sort(lst_no_duplicates, 0, len(lst_no_duplicates)-1)', number=1, globals=globals())
print('test array with NO duplicated elements')
print('quicksort: ', t_quicksort)
print('mergesort: ', t_mergesort)
