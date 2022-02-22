def merge(arr, p, q, r):
    left = arr[p:q]
    right = arr[q:r]
    i, j = 0, 0
    for k in range(p, r):
        if j == len(right):
            arr[k: k + len(left) - i] = left[i:len(left)]
            break
        elif i == len(left):
            arr[k: k + len(right) - j] = right[j:len(right)]
            break
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


arr = list(reversed(range(1, 10)))
x = 15

merge_sort(arr)
