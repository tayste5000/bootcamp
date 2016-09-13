import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Settings for plots
rc = {'lines.linewidth': 2,
    'axes.labelsize': 18,
    'axes.titlesize': 18}

sns.set(rc=rc)

def ecdf(data):
    '''
    Compute x, y values for an empirical distribution function
    '''

    x = np.sort(data)

    y = np.arange(0, 1, 1/len(x))

    return x, y

# Get the data
xa_high = np.loadtxt('data/xa_high_food.csv')
xa_low = np.loadtxt('data/xa_low_food.csv')

# Get the ecdf of each data set
x_high, y_high = ecdf(xa_high)
x_low, y_low = ecdf(xa_low)

# Clear figure
plt.close()

# Start new figures
fig = plt.figure(1)
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

ax1.plot(x_high, y_high, marker='.', linestyle='none', markersize=15, alpha=0.3)
ax1.set_xlabel('Cross-sectional area (um)')
ax1.set_ylabel('eCDF')
ax1.legend(('low food',), loc='lower right')
ax2.plot(x_low, y_low, marker='.', linestyle='none', markersize=15, alpha=0.3)
ax2.set_xlabel('Cross-sectional area (um)')
ax2.set_ylabel('eCDF')
ax2.legend(('high food',), loc='lower right')

plt.show()
