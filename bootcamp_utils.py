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
