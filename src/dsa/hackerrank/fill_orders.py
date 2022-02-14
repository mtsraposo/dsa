import random


def filled_orders(order, k):
    sorted_orders = sorted(order)
    middle = len(sorted_orders) // 2
    print(middle, k)
    left = sorted_orders[:middle]
    right = sorted_orders[middle:]
    if min(sorted_orders) > k:
        return 0
    else:
        if sum(sorted_orders) <= k:
            return len(sorted_orders)
        else:
            if sum(left) < k:
                return len(left) + filled_orders(right, k - sum(left))
            else:
                return filled_orders(left, k)


order = [random.randrange(1, 10 ** 9, 1) for i in range(2 * 10 ** 5)]
k = random.randint(1, 10 ** 9)
print(filled_orders(order, k))
