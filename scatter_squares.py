# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 13:40:03 2020

@author: Jake
"""

import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('fivethirtyeight')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap = plt.cm.Oranges, s=10)

#Scatter chart and label axes
ax.set_title('Square Numbers', fontsize = 24)
ax.set_xlabel('Value', fontsize = 14)
ax.set_ylabel('Square of Value', fontsize = 14)

#Set size fo tick labels
ax.tick_params(axis='both', which = 'major', labelsize = 14)

#Set range for each axis
ax.axis([0,1100,0,1100000])

plt.savefig('Squares_Plot.png', bbox_inches='tight')