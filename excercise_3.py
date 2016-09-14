'''
a) Load in the three data sets. They are in the files ~/git/data/wt_lac.csv,
~/git/data/q18m_lac.csv, and ~/git/data/q18a_lac.csv.
Be sure to check out the files on the command line
to see what kwargs you need for np.loadtxt() to load them in.

b) Make a plot of fold change IPTG concentration for each of the three mutants.
Think: should any of the axes have a logarithmic scale?

c) Write a function with the call signature
fold_change(c, RK, KdA=0.017, KdI=0.002, Kswitch=5.8)
to compute the theoretical fold change.
It should allow c, the concentration of IPTG, to be passed in as a NumPy array
or scalar, and RK, the  R/KR/K  ratio, must be a scalar. Remember,
with NumPy arrays, you don't have to write for loops to do operations
to each element of the array.

d) You will now plot a smooth curve showing the theoretical fold change for each mutant.
Make an array of closely spaced points for the IPTG concentration.
Hint: The function np.logspace() will be useful.
Compute the theoretical fold change based on the given parameters
using the function you wrote in part (c).
Plot the smooth curves on the same plot with the data.
Don't forget to annotate your plot with axis labels and a legend.

e) If we look at the functional form of the fold change and at
the parameters we are given, we see that only  R/KR/K  varies
from mutant to mutant. I told you this a priori, but we didn't really know it.
Daber, Sochol, and Lewis assumed that the binding to IPTG would be unaltered
and the binding to DNA would be altered based on the position of the mutation
in the lac repressor protein. Now, if this is true, then  R/KR/K  should be the
only thing that varies. We can check this by seeing if the data collapse onto a
single curve. To see how this works, we define the Bohr parameter,  F(c)F(c) , as
F(c)=−ln(R/K)−ln((1+c/KAd)2(1+c/KAd)2+Kswitch(1+c/KId)2).
F(c)=−ln⁡(R/K)−ln⁡((1+c/KdA)2(1+c/KdA)2+Kswitch(1+c/KdI)2).blah

The second term in the Bohr parameter is independent of the identity of the mutant,
and the first term depends entirely upon it. Then, the fold change can be written as
fold change=11+e−F(c).
fold change=11+e−F(c).

So, if we make our  xx -axis to be the Bohr parameter, all data should fall on
the same curve. Hence the term, data collapse. (The Bohr parameter gets its name
(as given by Rob Phillips) because it is inspired by the work of Christian Bohr
(Niels's father), who discovered similar families of curves describing binding of oxygen to hemoglobin.)
Now, we will plot the theoretical curve of fold change versus Bohr parameter.
Write a function with call signature bohr_parameter(c, RK, KdA=0.017, KdI=0.002, Kswitch=5.8)
that computes the Bohr parameter.
Write a function with call signature fold_change_bohr(bohr_parameter)
that gives the fold change as a function of the Bohr parameter.
Generate values of the Bohr parameter ranging from  −6−6  to  66
in order to make a smooth plot.
Compute the theoretical fold change as a function of the Bohr parameter
and plot it as a gray line using plt.plot()'s kwarg color='gray'.
f) Now, for each experimental curve:
Convert the IPTG concentration to a Bohr parameter using the given parameters.
Plot the experimental fold change versus the Bohr parameter you just calculated.
Plot the data as dots on the same plot that you made the universal gray curve.
Appropriately annotate your plot.
Do you see data collapse? Does it make sense the only binding to the operator is
changing from mutant to mutant? And importantly, the collapse demonstrates that
all of the mutants are behaving according to the Monod-Wyman-Changeux model,
and the mutations affect quantitative, not qualitative,
changes in the behavior of the repressor.
'''
import numpy as np

# This is how we import the module of Matplotlib we'll be using
import matplotlib.pyplot as plt

# Some pretty Seaborn settings
import seaborn as sns
rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)


def load_data():
    '''load data files into np arrays, return'''

    # File order is wt, q18m, q18a
    files = ('data/wt_lac.csv', 'data/q18m_lac.csv', 'data/q18a_lac.csv')

    # Map to loadtxt function
    data = map(lambda x: np.loadtxt(x, skiprows=3, delimiter=','), files)

    return tuple(data)


def fold_change(c, RK, KdA=0.017, KdI=0.002, Kswitch=5.8):
    '''
    Given concentration of a ligand, R/K, KdA, KdI, and Kswitch for a protein
    return the fold change in activation
    '''

    # Helper func to simplify a repeated expression
    def gt(k):
        return (1 + c/k)**2

    # Compute and return fold change
    return (1 + ( (RK * gt(KdA)) / (gt(KdA) + Kswitch * gt(KdI))))**-1

def bohr_parameter(c, RK, KdA=0.017, KdI=0.002, Kswitch=5.8):
    '''
    Given concentration of a ligand, R/K, KdA, KdI, and Kswitch for a protein
    return the bohr parameter in activation
    '''

    # Helper func to simplify a repeated expression
    def gt(k):
        return (1 + c/k)**2

    # Compute and return fold change
    return -1 * np.log(RK) - np.log((gt(KdA)) / (gt(KdA) + Kswitch * gt(KdI)))

def fold_change_bohr(bohr_parameter):
    '''given te bohr parameter, return the fold change'''

    return 1 / (1 + np.exp(-1 * bohr_parameter))



def plot_fold_change(data_tuple):
    '''plot the data points in a 3x1 graph'''

    # Initialize the figure
    fig = plt.figure(1)
    axes = fig.add_subplot(1, 1, 1)

    # R/K constants in the same order as the mutants
    RKs = [141.5, 1332, 16.56]

    # Iterate through data and plot
    for data, RK in zip(data_tuple, RKs):
        # Split into X and Y
        x_data = data[:,0]
        y_data = data[:,1]

        theoretical_y = fold_change(x_data, RK)

        axes.plot(x_data, y_data, linestyle='none', marker='.', markersize=15)
        axes.plot(x_data, theoretical_y)

    # Add labels, legends, and format
    axes.set_xscale('log')
    axes.set_title('Super Awesome Data')
    axes.set_xlabel('IPTG (mM)')
    axes.set_ylabel('Fold Change')
    axes.legend(('Wild Type', 'Q18M', 'Q18A'), loc='lower right')

    plt.show()

def plot_theoretical_bohr():
    '''Plot a theoretical curve of fold change vs bohr'''

    # Generate fake bohr data
    fake_bohr = np.linspace(-6,6)

    # Generate fake fold change data
    fake_fold_change = fold_change_bohr(fake_bohr)

    # Initialize the figure and plot
    fig = plt.figure(1)
    axes = fig.add_subplot(1, 1, 1)
    axes.plot(fake_bohr, fake_fold_change, color='gray')

    # Add labels, legends, and format
    axes.set_title('Super Awesome Data')
    axes.set_xlabel('Bohr parameter')
    axes.set_ylabel('Fold Change')

def plot_theoretical_bohr_and_data(data_tuple):
    '''Plot a theoretical curve of fold change vs bohr'''

    # Generate fake bohr data
    fake_bohr = np.linspace(-6,6)

    # Generate fake fold change data
    fake_fold_change = fold_change_bohr(fake_bohr)

    # R/K constants in the same order as the mutants
    RKs = [141.5, 1332, 16.56]

    # Initialize the figure and plot
    fig = plt.figure(1)
    axes = fig.add_subplot(1, 1, 1)

    # Iterate through data and plot
    for data, RK in zip(data_tuple, RKs):
        # Split into X and Y
        x_data = data[:,0]
        x_bohr = bohr_parameter(x_data, RK)

        y_data = data[:,1]

        axes.plot(x_bohr, y_data, linestyle='none', marker='.', markersize=15)

    axes.plot(fake_bohr, fake_fold_change, color='gray')

    # Add labels, legends, and format
    axes.set_title('Super Awesome Data')
    axes.set_xlabel('Bohr parameter')
    axes.set_ylabel('Fold Change')


'''
a) Now it's time to simulate the Lotka-Volterra model.
Since predator and prey both begin with "p,"
we'll call the predators foxes ( ff ) and the prey rabbits ( rr ).
The differential equation describing the dynamics of the rabbit population is
drdt=αr−βfr.

The first term at the right hand side is exponential growth,
the same you would expect for a growing bacterial colony.
The second term is killing off due to predation. If  ff  is large,
more rabbits get hunted down.
The differential equation describing the dynamics of the fox population is
dfdt=δfr−γf.

The first term represents growth in the fox population by consumption of rabbits.
The second term is the natural die-off of foxes.
Your task in this exercise is to numerically solve these two differential
equations together and then plot the result. Use the following parameter values
alpha = 1
beta = 0.2
delta = 0.3
gamma = 0.8
delta_t = 0.001
t = np.arange(0, 60, delta_t)
r[0] = 10
f[0] = 1

Even though there are now two differential equations,
the procedure is the same, you update each by adding
ΔtΔt  times the respective derivative.
When you plot the result, does it make sense?

b) [Bonus] It is probably the simplest way to solve differential equations,
and is by no means the best. SciPy has an ODE solver,
scipy.integrate.odeint() that uses the more sophisticated
and robust methods for solving systems of ODEs.
Read the documentation about how scipy.integrate.odeint()
works and use it to solve the Lotka-Volterra system of ODEs.
This problem is tough; I'm not giving you directions,
and you are kind of on your own to read the documentation and figure it out.
It may be useful to read this tutorial I wrote to help students solve ODEs
that come up in systems biology.
'''
from scipy.integrate import odeint

def sim_lotka_volterra():

    # All starting parameters
    alpha = 1
    beta = 0.2
    delta = 0.3
    gamma = 0.8

    # Time change intervals
    delta_t = 0.001

    # All time units
    t = np.arange(0, 60, delta_t)

    # Starting arrays for rabbit and fox population
    r = np.array([10])
    f = np.array([1])

    # Run simulation
    for nt in t[1:]:

        # Get most recent Rabbit and Fox population
        old_r = r[-1]
        old_f = f[-1]

        # Compute changes over nt
        dr = alpha * old_r - beta * old_f * old_r
        df = delta * old_r * old_f - gamma * old_f

        # Comput new values
        new_r = old_r + dr * delta_t
        new_f = old_f + df * delta_t

        # Add to array
        r = np.append(r, new_r)
        f = np.append(f, new_f)

    ### Plot results ###
    # Initialize the figure and plot
    fig = plt.figure(1)
    axes = fig.add_subplot(1, 1, 1)

    # Plot and format
    axes.plot(t, r)
    axes.plot(t, f)
    axes.set_title('Foxes R Hitler')
    axes.set_xlabel('Time')
    axes.set_ylabel('Population')
    axes.legend(('Rabits', 'Foxes'))

    plt.show()

def sim_lotka_scipy():
    # All starting parameters
    alpha = 1
    beta = 0.2
    delta = 0.3
    gamma = 0.8

    # Time change intervals
    delta_t = 0.001

    # All time units
    t = np.arange(0, 60, delta_t)

    # Starting arrays for rabbit and fox population
    r0 = 10
    f0 = 1

    # Define ODE system
    def ode_sys(y, t, alpha, beta, delta, gamma):
        # Get individual parameters from y
        r, f = y

        # Write expressions for dy
        dydt = [alpha * r - beta * f * r,
                delta * r * f - gamma * f]

        return dydt

    # Solve equation
    solution = odeint(ode_sys, [r0, f0], t, args=(alpha, beta, delta, gamma))

    ### Plot results ###
    # Initialize the figure and plot
    fig = plt.figure(1)
    axes = fig.add_subplot(1, 1, 1)

    # Plot and format
    axes.plot(t, solution[:, 0])
    axes.plot(t, solution[:, 1])
    axes.set_title('Foxes R Hitler')
    axes.set_xlabel('Time')
    axes.set_ylabel('Population')
    axes.legend(('Rabits', 'Foxes'))

    plt.show()
