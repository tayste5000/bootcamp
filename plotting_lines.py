import numpy as np
import scipy.special
import matplotlib.pyplot as plt
import seaborn as sns

# Generate an array of x values
x = np.linspace(-15, 15, 400)

# Compute the normalized intensity
norm_I = 4 * (scipy.special.j1(x) / x)**2

# Clear any existing figures
plt.close()

# Create figure
fig = plt.figure(1)
axes = fig.add_subplot(1,1,1)

# Plot our computation
axes.plot(x, norm_I, marker='.', linestyle='none')
axes.margins(0.02)
axes.set_xlabel('$x$')
axes.set_ylabel('$I(x) / I_0$')

# Processing the spike data
data = np.loadtxt('data/retina_spikes.csv', skiprows=2, delimiter=',')
t = data[:,0]
V = data[:,1]

# Clear any existing figures
plt.close()

# Create figure
fig = plt.figure(1)
axes = fig.add_subplot(1,1,1)

# Plot data
axes.plot(t, V)
axes.set_xlabel('t (ms)')
axes.set_ylabel('V (uV)')
axes.set_xlim(1395, 1400)

plt.show()
