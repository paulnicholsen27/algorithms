def mergesort(lst):
    '''Recursively divides list in halves to be sorted'''
    if len(lst) <= 1:
        return lst, 0
    middle = len(lst)/2
    left  = mergesort(lst[:middle])[0]
    right = mergesort(lst[middle:])[0]
    sortedlist = merge(left, right)
    return sortedlist

def merge(left, right):
    '''Subroutine of mergesort to sort split lists.  Also returns number
    of split inversions (i.e., each occurence of a number from the sorted second
    half of the list appearing before a number from the sorted first half)'''
    i, j = 0, 0
    splits = 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            splits += len(left[i:])
    result += left[i:]
    result += right[j:]
    print result, splits
    return result, splits


print mergesort([7,2,6,4,5,1,3,8])