import csv
from datetime import datetime
import matplotlib.pyplot as plt

file_name = 'data\sitka_weather_07-2018_simple.csv'
with open(file_name) as f:
    reader = csv.reader(f)
    header_row = next(reader)

#get the high temperatures and the dates
    highs = []
    dates = []
    for row in reader:
        high = int(row[5])
        highs.append(high)
        date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(date)

#Starting the plot
plt.style.use('bmh')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='orangered')

#formating plot
plt.title('Daily high temperatures, july 2018', fontsize=24)
plt.xlabel('Date', fontsize=16)
plt.ylabel('Temperature (°F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16 )
fig.autofmt_xdate()
plt.show()