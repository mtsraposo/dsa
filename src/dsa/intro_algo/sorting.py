from random import randint

import time

from copy import deepcopy


def print_running_time(command):
    start = time.time()
    exec(command)
    end = time.time()
    print(end - start)


def insertion_sort(arr, ascending=True):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and (arr[i] > key) is ascending:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = key
    return arr


def selection_sort(arr):
    for j in range(len(arr) - 1):
        min_e = arr[j]
        min_i = j
        for i in range(j + 1, len(arr)):
            if arr[i] < min_e:
                min_e = arr[i]
                min_i = i
        arr[j], arr[min_i] = min_e, arr[j]
    return arr


def merge(arr, p, q, r):
    left = arr[p:q]
    right = arr[q:r]
    i, j = 0, 0
    for k in range(p, r):
        if j == len(right):
            arr[k:k + len(left) - i - 1] = left[i + 1:len(left)]
        elif i == len(left):
            arr[k:k + len(right) - j - 1] = right[j + 1:len(right)]
        else:
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1


def merge_sort(arr, p=0, r=None):
    if r is None:
        r = len(arr)
    if r > p + 1:
        q = (p + r) // 2
        merge_sort(arr, p, q)
        merge_sort(arr, q, r)
        merge(arr, p, q, r)


def check_sorted(arr):
    # Return True if array is sorted
    return all([arr[i] <= arr[i + 1] for i in range(len(arr) - 1)])


if __name__ == '__main__':
    input_array = [randint(0, 10 ** 4) for i in range(10 ** 4)]
    arr = deepcopy(input_array)

    # The built-in sorted method is significantly faster than merge-sort, insertion and selection sort algorithms.
    # It uses the Timsort algorithm, a mixture between merge sort and insertion sort.
    print_running_time(command="sorted(deepcopy(input_array))")  # 0.00821375846862793
    print_running_time(command="merge_sort(arr=deepcopy(input_array))")  # 0.45260000228881836
    print_running_time(command="selection_sort(arr=deepcopy(input_array))")  # 1.6123661994934082
    print_running_time(command="insertion_sort(arr=deepcopy(input_array))")  # 2.6405270099639893

    # Descending order
    insertion_sort(arr=[5, 2, 4, 6, 1, 3],
                   ascending=False)
