import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats
from bootcamp_utils import ecdf

# Settings for plots
rc = {'lines.linewidth': 2,
    'axes.labelsize': 18,
    'axes.titlesize': 18}

sns.set(rc=rc)

# Get the data
xa_high = np.loadtxt('data/xa_high_food.csv')
xa_low = np.loadtxt('data/xa_low_food.csv')

# Get the ecdf of each data set
x_high, y_high = ecdf(xa_high)
x_low, y_low = ecdf(xa_low)

x = np.linspace(1600, 2500, 400)
cdf_high = scipy.stats.norm.cdf(x, loc=np.mean(xa_high), scale=np.std(xa_high))

cdf_low = scipy.stats.norm.cdf(x, loc=np.mean(xa_low), scale=np.std(xa_low))

# Clear figure
plt.close()

# Start new figures
fig = plt.figure(1)
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

ax1.plot(x_high, y_high, marker='.', linestyle='none', markersize=15, alpha=0.5)
ax1.plot(x, cdf_high, color='gray')
ax1.set_xlabel('Cross-sectional area (um)')
ax1.set_ylabel('eCDF')
ax1.legend(('low food',), loc='lower right')
ax2.plot(x_low, y_low, marker='.', linestyle='none', markersize=15, alpha=0.5)
ax2.plot(x, cdf_low, color='gray')
ax2.set_xlabel('Cross-sectional area (um)')
ax2.set_ylabel('eCDF')
ax2.legend(('high food',), loc='lower right')

plt.show()
