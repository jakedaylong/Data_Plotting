# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 15:23:50 2020

@author: Jake
"""

import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'weather_data_2020.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
    
    for index, column_header in enumerate(header_row):
        print(index, column_header)
        
    #get highs and lows
    dates = []
    highs = []
    lows = []
    for row in reader:
        current_date = datetime.strptime(row[5], '%m/%d/%Y')
        dates.append(current_date)
        high = int(row[6])
        highs.append(high)
        low = int(row[8])
        lows.append(low)
        

#plot temperatures
plt.style.use('fivethirtyeight')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha = 0.5, linewidth = 1)
ax.plot(dates, lows, c='blue', alpha = 0.5, linewidth = 1)
ax.fill_between(dates, highs, lows, facecolor = 'blue', alpha = 0.1)

ax.set_title('Highs and Lows for Everett - 2020', fontsize = 16)
ax.set_xlabel('', fontsize = 8)
fig.autofmt_xdate()
ax.set_ylabel('Tempurature - F', fontsize = 14)
ax.tick_params(axis = 'both', which = 'major', labelsize = 6)

#plt.show()
plt.savefig('Weather_Data.png', dpi=150, bbox_inches='tight')

print(highs)
print(lows)
print(dates)