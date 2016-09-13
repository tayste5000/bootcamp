import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Settings for plots
rc = {'lines.linewidth': 2,
    'axes.labelsize': 18,
    'axes.titlesize': 18}

sns.set(rc=rc)

data_txt = np.loadtxt('data/collins_switch.csv', skiprows=2, delimiter=',')

# Extract data
iptg = data_txt[:,0]
gfp = data_txt[:,1]

# Clear anything old
plt.close()

# Make figure
fig = plt.figure(1)
axes = fig.add_subplot(1,1,1)

# Errors
sem = data_txt[:,2]

# Plot iptg vs gfp
axes.errorbar(iptg, gfp, yerr=sem, linestyle='none', marker='.', markersize=20)
axes.set_xlabel('IPTG (mM)')
axes.set_ylabel('Normalized GFP')
axes.set_ylim(-0.02, 1.02)
axes.set_xlim(8e-4, 15)
axes.set_xscale('log')
axes.set_title('IPTG Titration')
plt.show()
