from src.dsa.intro_algo.chapter_2.searching import binary_search
from src.dsa.intro_algo.chapter_2.sorting import merge_sort



arr = list(reversed(range(1, 10)))
x = 15

merge_sort(arr)
for i in range(len(arr)):
    print(binary_search(arr[i+1:], x-i))
