'''
a) Load each of the files into separate Pandas DataFrames.
You might want to inspect the file first to make sure you know what
character the comments start with and if there is a header row.

b) We would like to merge these all into one DataFrame.
The problem is that they have different header names,
and only the 1973 file has a year entry (called yearband).
This is common with real data. It is often a bit messy and requires some munging.

First, change the name of the yearband column of the 1973 data to year.
Also, make sure the year format is four digits, not two!

Next, add a year column to the other four DataFrames.
You want tidy data, so each row in the DataFrame should have an entry for the year.

Change the column names so that all the DataFrames have the same column names.
I would choose column names
['band', 'species', 'beak length (mm)', 'beak depth (mm)', 'year']

Concatenate the DataFrames into a single DataFrame. Be careful with indices!
If you use pd.concat(), you will need to use the ignore_index=True kwarg.
You might also need to use the axis kwarg.'''

import pandas as pd
import numpy as np
import bootcamp_utils
import matplotlib.pyplot as plt

# Import data into pandas dataframes
df_1973 = pd.read_csv('data/grant_1973.csv', comment='#')
df_1975 = pd.read_csv('data/grant_1975.csv', comment='#')
df_1987 = pd.read_csv('data/grant_1987.csv', comment='#')
df_1991 = pd.read_csv('data/grant_1991.csv', comment='#')
df_2012 = pd.read_csv('data/grant_2012.csv', comment='#')

# Change yearband to year
df_1973.rename(columns={'yearband':'year'}, inplace=True)

# Fix year format
df_1973['year'] = df_1973['year'].apply(lambda x: '19' + str(x))

# Add year format to the rest
df_1975['year'] = pd.Series(np.repeat('1975', len(df_1975)), index=df_1975.index)
df_1987['year'] = pd.Series(np.repeat('1987', len(df_1987)), index=df_1987.index)
df_1991['year'] = pd.Series(np.repeat('1991', len(df_1991)), index=df_1991.index)
df_2012['year'] = pd.Series(np.repeat('2012', len(df_2012)), index=df_2012.index)

# Fix column names
df_1973.rename(columns={'beak length':'Beak length, mm', 'beak depth': 'Beak depth, mm'}, inplace=True)
df_1991.rename(columns={'blength':'Beak length, mm', 'bdepth': 'Beak depth, mm'}, inplace=True)
df_2012.rename(columns={'blength':'Beak length, mm', 'bdepth': 'Beak depth, mm'}, inplace=True)

# Concat everything
df_all = pd.concat([df_1973, df_1975, df_1987, df_1991, df_2012], ignore_index=True)

'''
c) The band fields gives the number of the band on the bird's leg
that was used to tag it. Are some birds counted twice?
Are they counted twice in the same year? Do you think you should drop
duplicate birds from the same year? How about different years
 My opinion is that you should drop duplicate birds from the
 same year and keep the others, but I would be open to discussion on that.
 To practice your Pandas skills, though, let's delete only duplicate birds
 from the same year from the DataFrame. When you have made this DataFrame,
 save it as a CSV file.
Hint: The DataFrame methods duplicated() and drop_duplicates() will be useful.
After doing this work, it is worth saving your tidy DataFrame in a CSV document.
To this using the to_csv() method of your DataFrame.
Since the indices are uninformative, you should use the index=False kwarg.
(I have already done this and saved it as ~/git/bootcamp/data/grant_complete.csv,
which will help you do the rest of the exercise if you have problems with this part.)

d) Plot an ECDF of beak depths of Geospiza fortis specimens measured in 1987.
Plot an ECDF of the beak depths of Geospiza scandens from the same year.
These ECDFs should be on the same plot. On another plot, plot ECDFs
of beak lengths for the two species in 1987. Do you see a striking phenotypic difference?

e) Perhaps a more informative plot is to plot the measurement of each bird's beak
as a point in the beak depth-beak length plane. For the 1987 data,
plot beak depth vs. beak width for Geospiza fortis as blue dots,
and for Geospiza scandens as red dots. Can you see the species demarcation?

f) Do part (e) again for all years. Describe what you see.
Do you see the changes in the differences between species
(presumably as a result of hybridization)?
In your plots, make sure all plots have the same range on the axes.'''

# Remove all band duplicates for the same year
df_all.drop_duplicates(subset=['band','year'], inplace=True)

# Get fortis 1987 data
fortis_1987 = df_all.loc[(df_all['year']=='1987') & (df_all['species']=='fortis'), ['Beak depth, mm']]

# Get ecdf data of 1987
x_ecdf, y_ecdf = bootcamp_utils.ecdf(fortis_1987)

# Plot ecdf datt
# plt.plot(x_ecdf, y_ecdf, linestyle='none', marker='.')
# plt.title('Fortis 1987')
# plt.show()
# plt.clf()

# Get fortis 1987 data for beak length
fortis_1987_bl = df_all.loc[(df_all['year']=='1987') & (df_all['species']=='fortis'), ['Beak length, mm']]

# Plot ecdf datt
# plt.plot(fortis_1987, fortis_1987_bl, linestyle='none', marker='.')
# plt.xlabel('Beak depth (mm)')
# plt.ylabel('Beak length (mm)')
# plt.title('Fortis 1987')

# Initialize figure
fig = plt.figure(1)

# Repeat plot for all years
for i, year in enumerate(['1973', '1975', '1987', '1991', '2012']):

    # Initialize specific plot
    axes = fig.add_subplot(2,3,i+1)

    # Split year data between fortis and scandens
    depth_data_fortis = df_all.loc[(df_all['year']==year) & (df_all['species']=='fortis'), ['Beak depth, mm']]
    length_data_fortis = df_all.loc[(df_all['year']==year) & (df_all['species']=='fortis'), ['Beak length, mm']]
    depth_data_scandens = df_all.loc[(df_all['year']==year) & (df_all['species']=='scandens'), ['Beak depth, mm']]
    length_data_scandens = df_all.loc[(df_all['year']==year) & (df_all['species']=='scandens'), ['Beak length, mm']]

    # Plot separately, format
    axes.plot(depth_data_fortis, length_data_fortis, linestyle='none', marker='.')
    axes.plot(depth_data_scandens, length_data_scandens, linestyle='none', marker='.')
    # axes.set_xlabel('Beak depth (mm)')
    # axes.set_ylabel('Beak length (mm)')
    axes.set_title(year)
    axes.legend(('fortis', 'scandens'), loc='lower right')
    axes.set_xlim((6,13))
    axes.set_ylim((9,16))

# It looks like the populations are getting closer
plt.show()
