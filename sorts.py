import math

######### INSERTION SORT ##########


def insertion_sort(arr):
    keycomp = 0

    for i in range(1, len(arr)):
        key = arr[i]  # Current element to be inserted into the sorted portion
        j = i - 1  # Index of the last element in the sorted portion

        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            keycomp += 1
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return keycomp


def count(k):
    k[0] += 1


######### MERGE SORT ##########


def merge_sort(arr, keycomp):
    if len(arr) > 1:
        # split part
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        keycomp += merge_sort(L, keycomp)
        keycomp += merge_sort(R, keycomp)

        # merge part
        l_counter = r_counter = arr_counter = 0

        while l_counter < len(L) and r_counter < len(R):
            keycomp += 1

            if L[l_counter] <= R[r_counter]:
                arr[arr_counter] = L[l_counter]
                l_counter += 1
            else:
                arr[arr_counter] = R[r_counter]
                r_counter += 1

            arr_counter += 1

        # clean up the remaining values
        while l_counter < len(L):
            arr[arr_counter] = L[l_counter]
            l_counter += 1
            arr_counter += 1

        while r_counter < len(R):
            arr[arr_counter] = R[r_counter]
            r_counter += 1
            arr_counter += 1

    return keycomp


######### MERGE SORT IN PLACE ##########


def merge_sort2(arr, start, end, k):
    if start < end:
        # split part
        mid = (start + end) // 2

        merge_sort2(arr, start, mid, k)
        merge_sort2(arr, mid + 1, end, k)

        # merge part
        a = start
        b = mid + 1
        if end < start:
            return
        while a <= mid and b <= end:
            count(k)
            if arr[a] >= arr[b]:  # swap item at a with item at b
                if a == mid + 1 and b == end:
                    break
                temp = arr[b]
                b += 1
                for i in range(b - 1, a, -1):  # shift all items up by 1
                    arr[i] = arr[i - 1]
                arr[a] = temp
                mid += 1
            else:
                a += 1

    return


######### QUICK SORT ##########


def quick_sort(arr, start, end):
    # base case
    if start >= end:
        return
    else:
        # get pivot
        pivot_position = partition(arr, start, end)
        # recursive call
        quick_sort(arr, start, pivot_position - 1)
        quick_sort(arr, pivot_position + 1, end)
    return


def partition(arr, start, end):
    pivot = arr[end]
    i = start - 1
    for j in range(start, end):
        if arr[j] < pivot:
            i += 1
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
    i += 1
    temp = arr[i]
    arr[i] = pivot
    arr[end] = temp
    return i


######### HEAP SORT ##########


def heapify(arr, n, i):  # MAX
    largest = i
    L = (i * 2) + 1  # left child
    R = (i * 2) + 2  # right child

    if L < n and arr[largest] < arr[L]:
        largest = L
    if R < n and arr[largest] < arr[R]:
        largest = R

    if largest != i:
        # if one of the child was bigger, child takes over, and heapify the new position
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # build heap
    for i in range(n // 2 - 1, -1, -1):
        # heapify from last parent to the top
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        # swap biggest with last item, then heapify up till last item
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


######### MAIN ##########


def generate_descending(n):
    return list(range(n, 0, -1))


test_array = [10, 9, 6, 5, 2, 1, 8, 7, 4, 3, 11]
keycomp = insertion_sort(test_array)
print("Insertion sort Key comparisons:", keycomp)

merge_test = [14, 40, 31, 28, 3, 15, 17, 51]
keycomp = [0]
merge_sort2(merge_test, 0, len(merge_test) - 1, keycomp)
print("Merge sort", merge_test, "Key comps:", keycomp)

quick_test = [2, 4, 1, 5, 3, 6, 9, 8, 7, 0, 12, 32, 1, 22, 3]
quick_sort(quick_test, 0, len(quick_test) - 1)
print("Quick sort", quick_test)

heap_test = [1, 2, 3, 4, 5, 6, 7]
heap_sort(heap_test)
print(heap_test)
