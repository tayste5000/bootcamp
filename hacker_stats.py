import numpy as np

# This is how we import the module of Matplotlib we'll be using
import matplotlib.pyplot as plt

# Some pretty Seaborn settings
import seaborn as sns
rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

bd_1975 = np.loadtxt('data/beak_depth_scandens_1975.csv')
bd_2012 = np.loadtxt('data/beak_depth_scandens_2012.csv')

# Generate Bootstrap
n_reps = 100000
bs_replicates_1975 = np.empty(n_reps)

for i in range(n_reps):
    bs_sample = np.random.choice(bd_1975, replace=True, size=len(bd_1975))
    bs_replicates_1975[i] = np.std(bs_sample)

# Generate Bootstrap
n_reps = 100000
bs_replicates_2012 = np.empty(n_reps)

for i in range(n_reps):
    bs_sample = np.random.choice(bd_2012, replace=True, size=len(bd_2012))
    bs_replicates_2012[i] = np.std(bs_sample)

def ecdf(data):
    return np.sort(data), np.arange(1, len(data) + 1) / len(data)

# x_1975, y_1975 = ecdf(bd_1975)
# x_1975_bs, y_1975_bs = ecdf(bs_sample)
# x_2012, y_2012 = ecdf(bd_2012)
# plt.plot(x_1975, y_1975, marker='.', linestyle='none')
# plt.plot(x_1975_bs, y_1975_bs, marker='.', linestyle='none', alpha=0.5)
# #plt.plot(x_2012, y_2012, marker='.', linestyle='none')
# plt.xlabel('beak depth (mm)')
# plt.ylabel('ECDF')
# plt.legend(('1975', '1975 Bootstrap'), loc='lower right')
# plt.show()
