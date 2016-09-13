import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure, show
import seaborn as sns

# Matplotlib settings
rc = {'lines.linewidth': 2,
    'axes.labelsize': 18,
    'axes.titlesize': 18}

sns.set(rc=rc)

# Get the data
xa_high = np.loadtxt('data/xa_high_food.csv')
xa_low = np.loadtxt('data/xa_low_food.csv')

# Make the figure and axes
fig = figure(1)
axes = fig.add_subplot(1,1,1)
#axes2 = fig.add_subplot(1,2,2)

# Make the bin boundaries.
low_min = np.min(xa_low)
low_max = np.max(xa_low)
high_min = np.min(xa_high)
high_max = np.max(xa_high)
global_min = np.min([low_min, high_min])
global_max = np.max([low_max, high_max])
bins = np.arange(global_min-50, global_max+50, 50)

# Create the histogram
# _ = axes.hist((xa_low, xa_high), bins=bins)
# axes.set_xlabel('Cross-sectional area (um$^2$)')
# axes.set_ylabel('count', rotation='horizontal')
_ = axes.hist(xa_low, normed=True, bins=bins, histtype='stepfilled', alpha=0.5)
_ = axes.hist(xa_high, normed=True, bins=bins, histtype='stepfilled', alpha=0.5)
axes.set_xlabel('Cross-sectional area (um$^2$)')
axes.set_ylabel('frequency')
axes.legend(('low concentration', 'high concentration'), loc='upper right')

# _ = axes2.hist(xa_high, bins=bins)
# axes2.set_xlabel('Cross-sectional area (um$^2$)')
# axes2.set_ylabel('count', rotation='horizontal')

show()

plt.savefig('egg_pdf_test.pdf', bbox_inches='tight')
