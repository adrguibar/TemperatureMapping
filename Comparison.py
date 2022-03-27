import csv
from datetime import datetime
import matplotlib.pyplot as plt

def get_data_from_file(file_path,highs, lows, dates):
    with open(file_path) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        date_index = header_row.index('DATE')
        tmax_index = header_row.index('TMAX')
        tmin_index = header_row.index('TMIN')
    #get the high temperatures and the dates
        for row in reader:
            date = datetime.strptime(row[date_index], '%Y-%m-%d')
            try:
                high = int(row[tmax_index])
                low = int(row[tmin_index])
            except ValueError:
                print('No value found')
            else:
                highs.append(high)
                lows.append(low)
                dates.append(date)

file1 = 'data/sitka_weather_2018_simple.csv'
highs,lows,dates = [],[],[]
sitka = get_data_from_file(file1,highs,lows,dates)

#Starting the plot 1
plt.style.use('bmh')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='orangered', alpha=0.8, label='High')
ax.plot(dates, lows, color='blue', alpha=0.8, label='Low')
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.2)



file2 = 'data/death_valley_2018_simple.csv'
highs,lows,dates = [],[],[]
sitka = get_data_from_file(file2,highs,lows,dates)
print(highs)
#Starting the plot 2
ax.plot(dates, highs, color='orangered', alpha=0.8, label='High')
ax.plot(dates, lows, color='blue', alpha=0.8, label='Low')
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.2)


#formating plot
plt.title('Daily high and low temperatures, 2018\nSitka, Alaska and Death '
          'Valley, California', fontsize=24)
plt.xlabel('Date', fontsize=16)
plt.ylabel('Temperature (°F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16 )
fig.autofmt_xdate()
plt.ylim(10,130)
plt.show()
