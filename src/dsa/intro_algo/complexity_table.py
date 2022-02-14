import math
import numpy as np
from scipy.optimize import minimize
from pynverse import inversefunc
import logging
import warnings

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
complexities = {'lg n': lambda n: np.log(n + 10 ** -12),
                'sqrt(n)': lambda n: np.sqrt(n),
                'n': lambda n: n,
                'n lg n': lambda n: n * np.log(n + 10 ** -12),
                'n**2': lambda n: n ** 2,
                'n**3': lambda n: n ** 3,
                '2**n': lambda n: 2 ** n,
                'n!': lambda n: math.factorial(n)}


def minimize_naive(fun, t, n_threshold):
    eval_fun = [(n, fun(n)) for n in range(n_threshold)]
    return next(filter(lambda e: e[1] > t, eval_fun))[0]


def find_upper_bound(fun, t, t_threshold=10 ** 16, n_threshold=30):
    # To avoid calculating excessively large numbers,
    # cap at max_n
    if fun(100) > t_threshold:
        return np.inf

    # If the function explodes too quickly, proceed with naïve
    # minimization instead of finding inverse or optimizing.
    if fun(n_threshold) > t:
        return minimize_naive(fun, t, n_threshold)

    # Try to find explicit inverse function,
    # otherwise, find an approximation
    try:
        inv = inversefunc(fun)
        return inv(t)
    except:
        logging.warning('Could not find inverse function. Proceed to approximation.')
        eq_fun = lambda n: fun(n) - t
        x0 = np.sqrt(t)
        sol = minimize(fun=eq_fun,
                       x0=np.array([x0]),
                       bounds=[(0, None)],
                       constraints={'type': 'ineq',
                                    'fun': eq_fun},
                       options={'maxiter': 1000,
                                'disp': True}  # Signal convergence
                       )
        return math.floor(sol.x[0])


warnings.filterwarnings('ignore')
print('Time  |', '  |  '.join([f'{t:.2E}' for t in time_frames.values()]))
for c_name, c_fun in complexities.items():
    print(c_name, end='')
    for t in time_frames.values():
        problems_solved = find_upper_bound(fun=c_fun, t=t)
        if problems_solved == np.inf:
            print(f' |    inf   ', end=' ')
        else:
            print(f' |  {problems_solved:.2E}', end=' ')
    print('\n')
warnings.filterwarnings('defaul')
