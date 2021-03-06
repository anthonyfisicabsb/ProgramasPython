import csv

from matplotlib import pyplot as plt
from datetime import datetime

filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs = [], []
    for rows in reader:
        current_date = datetime.strptime(rows[0], "%Y-%m-%d")
        dates.append(current_date)

        high = int(rows[1])
        highs.append(high)

        fig = plt.figure(dpi=128, figsize=(10, 6))
        plt.plot(dates, highs, c='red')

        plt.title("Daily high temperatures, July 24", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel('Temperature(F)', fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)

        plt.show()
