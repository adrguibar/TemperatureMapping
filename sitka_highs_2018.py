import csv
from datetime import datetime
import matplotlib.pyplot as plt

file_name = 'data\sitka_weather_2018_simple.csv'
with open(file_name) as f:
    reader = csv.reader(f)
    header_row = next(reader)

#get the high temperatures and the dates
    highs = []
    dates = []
    lows = []
    for row in reader:
        high = int(row[5])
        highs.append(high)
        low = int(row[6])
        lows.append(low)
        date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(date)

#Starting the plot
plt.style.use('bmh')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='orangered', alpha=0.8, label='High')
ax.plot(dates, lows, color='blue', alpha=0.8, label='Low')
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.2)
ax.legend()
#formating plot
plt.title('Daily high and low temperatures, 2018', fontsize=24)
plt.xlabel('Date', fontsize=16)
plt.ylabel('Temperature (°F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16 )
fig.autofmt_xdate()
plt.show()