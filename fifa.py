import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

full = pd.read_csv("C:/Users/admin/Downloads/fifa-18-demo-player-dataset/CompleteDataset.csv", index_col = 0, low_memory = False)
partial = pd.read_csv("C:/Users/admin/Downloads/fifa-18-demo-player-dataset/PartialDataset.csv", index_col = 0, low_memory = False)

# Fetch details of a player by searching name
print(full.loc[full['Name'] == 'S. Aguero'])

# Pandas Series
print(full.loc[full['Name'] == 'A. Sanchez']['Acceleration'])

# Pandas DataFrames
print(full.loc[full['Name'] == 'De Gea'][['Acceleration', 'Finishing']])

# Analysis Starts

part = np.array(partial['Overall'])

# Mean Overall of top 1000 players
ovr = np.array(full['Overall'])
mn = np.mean(ovr)
print('Mean = ', str(mn))

# Median Overall of top 1000 players
md = np.median(ovr)
print('Median = ', str(md))

# Similar Mean and Median show consistency of data

# Frequency of players in various categories

plt.rcParams["patch.force_edgecolor"] = True
plt.hist(ovr, bins=5, range = (50, 100), color='Orange', edgecolor='Blue')

# Add grid() call
# plt.grid(True)

# Strings
xlab = 'Overall Rating'
ylab = 'Number of Players'
title = 'FIFA 18 Player Distribution'

# Add axis labels
plt.xlabel(xlab)
plt.ylabel(ylab)

# Add title
plt.title(title)

plt.show()
plt.clf()

# Frequency of top 1000 players

plt.rcParams["patch.force_edgecolor"] = True
plt.hist(part, bins=6, range = (70, 100), color='Green', edgecolor='Red')

# Add axis labels
plt.xlabel(xlab)
plt.ylabel(ylab)

# Add title
plt.title(title)

plt.show()
plt.clf()
