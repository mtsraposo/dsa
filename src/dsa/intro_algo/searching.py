def linear_search(arr, v):
    for j in range(len(arr)):
        if arr[j] == v:
            return j
    return None


def binary_search(sorted_arr, v):
    midpoint = len(sorted_arr) // 2
    if len(sorted_arr) <= 1:
        return midpoint
    elif v == sorted_arr[midpoint]:
        return midpoint
    elif v > sorted_arr[midpoint]:
        return midpoint + 1 + binary_search(sorted_arr[midpoint + 1:], v)
    else:
        return binary_search(sorted_arr[:midpoint], v)


if __name__ == '__main__':
    linear_search(arr=[5, 2, 4, 6, 1, 3],
                  v=7)

    binary_search(sorted_arr=[1, 2, 3, 6, 9, 12, 15, 18, 21],
                  v=17)
