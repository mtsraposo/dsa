import time


def print_running_time(command):
    start = time.time()
    exec(command)
    end = time.time()
    print(end - start)


def insertion_sort(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = key
    return arr


if __name__ == '__main__':
    # The built-in sorted method is significantly faster than the insertion sort.
    # It uses the Timsort algorithm, a mixture between merge sort and insertion sort.
    print_running_time(command="insertion_sort(arr=[5, 2, 4, 6, 1, 3])")  # 4.70e-05
    print_running_time(command="sorted([5, 2, 4, 6, 1, 3])")  # 3.20e-05
