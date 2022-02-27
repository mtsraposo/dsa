import random
from collections import deque


def pile_cubes(d, n, base=0):
    for _ in range(n):
        if len(d) == 0 or (len(d) == 1 and (d[0] <= base or base == 0)):
            return True
        if (d[0] <= base and d[-1] <= base) or base == 0:
            if d[0] == d[-1]:
                d.pop()
                base = d.popleft()
            elif d[0] > d[-1]:
                base = d.popleft()
            else:
                base = d.pop()
        elif d[0] > base >= d[-1]:
            base = d.pop()
        elif d[0] <= base < d[-1]:
            base = d.popleft()
        else:
            return False


if __name__ == '__main__':
    n = 10 ** 5
    d = deque([random.randint(1, 2 ** 31) for _ in range(n)])
    pile_cubes(d, n)
