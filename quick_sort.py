import random

unsorted = [random.randint(1,200) for _ in range(20)]


def quick_sort(lst):
	if len(lst) <= 1:
		return lst
	else:
		pivot = lst[0]
		higher = quick_sort([x for x in lst[1:] if x>pivot])
		lower = quick_sort([x for x in lst[1:] if x<=pivot])
		return lower + [pivot] + higher

print quick_sort(unsorted)==sorted(unsorted)
print quick_sort(unsorted)
