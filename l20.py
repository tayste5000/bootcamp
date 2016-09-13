import numpy as np

xa_high = np.loadtxt('data/xa_high_food.csv')
xa_low = np.loadtxt('data/xa_low_food.csv')

def xa_to_diameter(xa)
    '''Docstring'''

    # Compute diameter from area
    # A = pi * d^2 / 4


    get_diameter = np.vectorize(lambda x: np.sqrt(4 * x / np.pi))
