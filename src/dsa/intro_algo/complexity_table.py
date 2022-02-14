import math
import numpy as np
from scipy.optimize import minimize
from pynverse import inversefunc

# <<< COMPARING SEVERAL COMPLEXITIES >>>

# Time in microseconds
second = 1 * 10 ** 6
minute = 60 * second
hour = 60 * minute
day = 24 * hour
month = 30 * day
year = 365 * day
century = 1000 * year
time_frames = {'1 second': second,
               '1 minute': minute,
               '1 hour': hour,
               '1 day': day,
               '1 month': month,
               '1 year': year,
               '1 century': century}

# Complexity functions
# Adding 10e-12 to log to avoid evaluating on zero
complexities = [lambda n: np.log(n + 10 ** -12),
                lambda n: np.sqrt(n),
                lambda n: n,
                lambda n: n * np.log(n + 10 ** -12),
                lambda n: n ** 2,
                lambda n: n ** 3,
                lambda n: 2 ** n,
                lambda n: math.factorial(n)]


# Try to find explicit inverse function,
# otherwise, find an approximation
def find_upper_bound(fun, t, max_n=10 ** 16):
    # To avoid calculating excessively large numbers,
    # cap at max_n
    if fun(max_n) < t:
        return np.inf

    try:
        inv = inversefunc(fun)
        return inv(t)
    except:
        eq_fun = lambda n: fun(n) - t
        x0 = np.sqrt(t)
        sol = minimize(fun=eq_fun,
                       x0=np.array([x0]),
                       bounds=[(0, None)],
                       constraints={'type': 'ineq',
                                    'fun': eq_fun})
        return math.floor(sol.x[0])


print('Time |', '  |  '.join([str(t) for t in time_frames.values()]))
for c in complexities:
    print('     ', end='')
    for t in time_frames.values():
        problems_solved = find_upper_bound(fun=c, t=t)
        print(f' |  {problems_solved:e}', end='')
    print('\n')
