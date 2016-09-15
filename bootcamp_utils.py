'''
bootcamp_utils: A collection of statistical functions proved useful for 55 students
'''

import numpy as np

def ecdf(data):
    '''
    Compute x, y values for an empirical distribution function
    '''

    x = np.sort(data)

    y = np.arange(0, 1, 1/len(x))

    return x, y

def do_bootstrap_func(data, func, size=1):
    '''function that draw bs replicates,
    performs a given function on the result, the returns it'''

    # Process with function
    output = np.empty(size)

    for i in range(size):
        # Do Bootstrap
        bs_sample = np.random.choice(data, replace=True, size=len(data))

        # Apply function
        output[i] = func(bs_sample)

    return output

def do_bootstrap(data, size=1):
    '''function that draw bs replicates,
    performs a given function on the result, the returns it'''

    # Process with function
    output = np.empty([size, len(data)])

    for i in range(size):
        # Do Bootstrap
        bs_sample = np.random.choice(data, replace=True, size=len(data))

        # Apply function
        output[i] = bs_sample

    return output
