'''
So, we seek the probability distribution of backtrack times,
P(tbt)P(tbt) , where  tbttbt  is the time spent in the backtrack.
We could solve this analytically, which requires some sophisticated mathematics.
But, because we know how to draw random numbers,
we can just compute this distribution directly using Monte Carlo simulation!
We start at  x=0x=0  at time  t=0t=0
We "flip a coin," or choose a random number to decide whether we step left or right.
We do this again and again, keeping track of how many steps we take and what the
xx  position is. As soon as  xx  becomes positive, we have existed the backtrack.
The total time for a backtrack is then  τnstepsτnsteps ,
where  ττ  is the time it takes to make a step. Depken, et al., report that  τ≈0.5 seconds.

a) Write a function, backtrack_steps(),
that computes the number of steps it takes for a random walker
(i.e., polymerase) starting at position  x=0x=0  to get to position  x=+1.
It should return the number of steps to take the walk.

b) Generate 10,000 of these backtracks in order to get enough samples out of  P(tbt).
(If you are interested in a way to really speed up this calculation, ask me about Numba.)

c) Use plt.hist() to plot a histogram of the backtrack times.
Use the normed=True kwarg so it approximates a probability distribution function.

d) You saw some craziness in part (c).
That is because, while most backtracks are short, some are reeeally long.
So, instead, generate an ECDF of your samples and plot the ECDF with the  xx  axis on a logarithmic scale.
'''
import numpy as np
import numba
import bootcamp_utils
import matplotlib.pyplot as plt

# Function to calculate the number of steps in the random walk
@numba.jit(nopython=True)
def backtrack_steps():

    # Initialize position and steps
    position = 0
    steps = 0

    # Simulate until steps = 1
    while position < 1:
        # Either go forwards or backwards
        position += np.random.choice(np.array([-1,1]))
        steps += 1

    return steps

# Function to perform n number of random walks
def n_backtracks(n):

    # Initialize results array
    results = np.empty(n)

    # Populate with data
    for i in range(len(results)):
        results[i] = backtrack_steps()

    return results

# Get data from 10000 backtracks
many_backtracks = n_backtracks(10000)

# Get eCDF of data
x_ecdf, y_ecdf = bootcamp_utils.ecdf(many_backtracks)

plt.plot(x_ecdf, y_ecdf)
plt.xscale('log')
plt.title('eCDF of 10,000 Random RNAp walks')
plt.show()
