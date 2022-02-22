import numpy as np


# <<< COMPARING COMPLEXITIES PAIRWISE >>>
# Find lowest n for which first function runs faster than second function
def find_equivalent_complexity(f1, f2, max_n=50):
    complexities = [(n, f1(n), f2(n)) for n in np.arange(1, max_n)]
    lower_complexities = filter(lambda c: c[1] < c[2], complexities)
    return next(lower_complexities)[0] - 1


# Examples
find_equivalent_complexity(f1=lambda n: 100 * n ** 2,
                           f2=lambda n: 2 ** n)
# >>> 14

find_equivalent_complexity(f1=lambda n: 8 * n ** 2,
                           f2=lambda n: 64 * n * np.log(n))
# >>> 1
