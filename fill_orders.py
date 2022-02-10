import random

def filledOrders(order, k):
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
                return len(left) + filledOrders(right, k-sum(left))
            else:
                return filledOrders(left, k)

# order = open('./sample_input.txt', 'r').read().split('\n')
# order = [int(i) for i in order]
#
# count = order.pop(0)
# k = order.pop(-1)

order = [random.randrange(1, 10**9, 1) for i in range(2*10**5)]
k = random.randint(1, 10**9)
print(filledOrders(order, k))