from src.dsa.intro_algo.chapter_2 import searching
from src.dsa.intro_algo.chapter_2 import sorting


def find_sum(arr, v):
    """
    Merge sort has a worst-case running time of O(n * lg n),
    while binary_search has a worst-case running time of O(log n),
    so find_sum will have a worst-case running time of:
    O(n * lg n) + n * O(log n) = O(n * lg n)
    """
    sorting.merge_sort(arr)
    for i in range(len(arr) - 1):
        if searching.binary_search(arr[i + 1:], v - arr[i]) != -1:
            return True
    return False


if __name__ == '__main__':
    print(find_sum(arr=list(reversed(range(1, 10))),
                   v=16))  # True
    print(find_sum(arr=list(reversed(range(1, 10))),
                   v=17))  # True
    print(find_sum(arr=list(reversed(range(1, 10))),
                   v=18))  # False
