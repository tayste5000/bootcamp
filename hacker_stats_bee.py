'''
Neonicotinoid pesticides are thought to have inadvertent effects
on service-providing insects such as bees.
A recent study of this was recently featured in the New York Times.
The original paper is Straub, et al., Proc. Royal Soc. B 283(1835): 20160506.
Straub and coworkers put their data in the Dryad repository,
which means we can work with it!
(Do you see a trend here? If you want people to think deeply about your results,
explore them, learn from them, in general further science with them,
make your data publicly available. Strongly encourage the members of your lab to do the same.)

We will look at the weight of drones (male bees) using the data set stored in
~/git/bootcamp/data/bee_weight.csv and the sperm quality of drone bees using
the data set stored in ~/git/bootcamp/data/bee_sperm.csv.

a) Load the drone weight data in as a Pandas DataFrame.
b) Plot ECDFs of the drone weight for control and also for those exposed to pesticide.
Do you think there is a clear difference?
c) Compute the mean drone weight for control and those exposed to pesticide.
Compute 95% bootstrap confidence intervals on the mean.
d) Repeat parts (a)-(c) for drone sperm. Use the 'Quality' column as your measure.
This is defined as the percent of sperm that are alive in a 500 µL sample.
e) As you have seen in your analysis in part (d), both the control and pesticide
treatments have some outliers with very low sperm quality.
This can tug heavily on the mean. So, get 95% bootstrap confidence intervals
for the median sperm quality of the two treatments.'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import bootcamp_utils

# Load drone weights
drones = pd.read_csv('data/bee_weight.csv', comment='#')

# Separate into pesticide and control
drone_pesticide = drones.loc[drones['Treatment']=='Pesticide', ['Weight']]
drone_control = drones.loc[drones['Treatment']=='Control', ['Weight']]

# Plot eCDFs
# x_ecfd_pesticide, y_ecdf_pesticide = bootcamp_utils.ecdf(drone_pesticide['Weight'])
# x_ecfd_control, y_ecdf_control = bootcamp_utils.ecdf(drone_control['Weight'])
# plt.plot(x_ecfd_control, y_ecdf_control)
# plt.plot(x_ecfd_pesticide, y_ecdf_pesticide)
# plt.legend(('Control', 'Pesticide'))
# plt.show()

# Compute the mean drone weights
print('The mean weight for control is:', np.mean(drone_control['Weight']))
print('The mean weight for pesticide is:', np.mean(drone_pesticide['Weight']))

# Bootstrap each 10000x and get mean
pesticide_bs_mean = bootcamp_utils.do_bootstrap_func(drone_pesticide['Weight'], np.mean, size=10000)
control_bs_mean = bootcamp_utils.do_bootstrap_func(drone_control['Weight'], np.mean, size=10000)

# Print the percentiles
print('The mean confidence interval for control is:', np.percentile(control_bs_mean, (2.5, 97.5)))
print('The mean confidence interval for pesticide is:', np.percentile(pesticide_bs_mean, (2.5, 97.5)))

# Load drone weights
sperm = pd.read_csv('data/bee_sperm.csv', comment='#')

# Remove rows where quality is NaN
sperm = sperm[np.isfinite(sperm['Quality'])]

# Separate into pesticide and control
sperm_pesticide = sperm.loc[sperm['Treatment']=='Pesticide', ['Quality']]
sperm_control = sperm.loc[sperm['Treatment']=='Control', ['Quality']]

# Plot eCDFs
x_ecfd_pesticide, y_ecdf_pesticide = bootcamp_utils.ecdf(sperm_pesticide['Quality'])
x_ecfd_control, y_ecdf_control = bootcamp_utils.ecdf(sperm_control['Quality'])
plt.plot(x_ecfd_control, y_ecdf_control)
plt.plot(x_ecfd_pesticide, y_ecdf_pesticide)
plt.legend(('Control', 'Pesticide'))
plt.show()

# Compute the mean sperm weights
print('The mean quality for control is:', np.mean(sperm_control['Quality']))
print('The mean quality for pesticide is:', np.mean(sperm_pesticide['Quality']))

# Bootstrap each 10000x and get mean
pesticide_bs_mean_sperm = bootcamp_utils.do_bootstrap_func(sperm_pesticide['Quality'], np.mean, size=10000)
control_bs_mean_sperm = bootcamp_utils.do_bootstrap_func(sperm_control['Quality'], np.mean, size=10000)

# Print the percentiles
print('The mean confidence interval for control is:', np.percentile(control_bs_mean_sperm, (2.5, 97.5)))
print('The mean confidence interval for pesticide is:', np.percentile(pesticide_bs_mean_sperm, (2.5, 97.5)))

# Bootstrap each 10000x and get mean
pesticide_bs_median_sperm = bootcamp_utils.do_bootstrap_func(sperm_pesticide['Quality'], np.median, size=10000)
control_bs_median_sperm = bootcamp_utils.do_bootstrap_func(sperm_control['Quality'], np.median, size=10000)

# Print the percentiles
print('The median confidence interval for control is:', np.percentile(control_bs_median_sperm, (2.5, 97.5)))
print('The median confidence interval for pesticide is:', np.percentile(pesticide_bs_median_sperm, (2.5, 97.5)))
