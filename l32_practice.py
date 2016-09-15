import numpy as np
import pandas as pd

################
### Practice ###
################

# Extract initial data
df = pd.read_csv('data/frog_tongue_adhesion.csv', comment='#')

# Extract the impact time of all impacts w/ adhesive strength > 2000 Pa.
imp_hi_adh = df.loc[df['adhesive strength (Pa)'] < -2000, ['impact time (ms)']]

# Extract the impact force and adhesive force for all of Frog II's strikes
f2_imp_and_adh = df.loc[df['ID']=='II',['impact force (mN)', 'adhesive force (mN)']]

# Extract the adhesive force and the time the frog pulls on the target for juvenile frogs
f3_4_adh_pull = df.loc[(df['ID']=='III') | (df['ID']=='IV'), ['adhesive force (mN)', 'time frog pulls on target (ms)']]

######################
### Group by intro ###
######################

# All frog ids
frogs = ['I', 'II', 'III', 'IV']

# Initialize empty dict for storing each frogs values
averages = np.empty(4)

# Split into groups by ID, comput average, and store
for i, id in enumerate(frogs):
    group = df.loc[df['ID']==id, :]
    averages[i] = np.mean(group['impact force (mN)'])

# We only want ID's and impact forces, so slice those out
df_impf = df.loc[:, ['ID', 'impact force (mN)']]

# Make a GroupBy object
grouped = df_impf.groupby('ID')

# Apply the np.mean function to the grouped object
df_mean_impf = grouped.apply(np.mean)

#########################
### Group by practice ###
#########################

# Compute standard deviation of the impact forces for each frog
df_std_impf = grouped.apply(np.std)

# Write a function, coeff_of_var(data),
# which computes the coefficient of variation of a data set.
# This is the standard deviation divided by the absolute value of the mean.
def coeff_of_var(data):
    '''Compute the coefficient of variation'''
    return np.std(data) / np.abs(np.mean(data))

# Compute a DataFrame w/ mean, median, std, and coeff_of_var
# of the impact forces and adhesive forces for each frog.

# Get a dataframe with impact force and adhesive force
df_impf_2 = df.loc[:, ['ID', 'impact force (mN)', 'adhesive force (mN)']]

# Turn into a groupby id dataframe
grouped_2 = df_impf_2.groupby('ID')

# Apply these functions
df_stuff_impf = grouped_2.agg([np.mean, np.median, np.std, coeff_of_var])
