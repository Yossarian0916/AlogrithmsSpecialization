# insertion sort
def insertion_sort(lst):

	for i in range(1, len(lst)):
		# insert key into sorted subarray
		card = lst[i]

		j = i-1
		while j >= 0 and lst[j] > card:
			lst[j+1] = lst[j]
			j = j-1
		lst[j+1] = card


if __name__ == '__main__':
	lst = [8,7,3,6,3,2]
	insertion_sort(lst)
	print(lst)