def linear_search(arr, v):
    for j in range(len(arr)):
        if arr[j] == v:
            return j
    return None


if __name__ == '__main__':
    linear_search(arr=[5, 2, 4, 6, 1, 3],
                  v=7)
