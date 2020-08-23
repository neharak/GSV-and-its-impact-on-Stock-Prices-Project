from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib import dates, pyplot
import csv
from collections import defaultdict
import numpy

columns = defaultdict(list)
with open('./SGSV values.csv') as f:
	reader = csv.DictReader(f)
	for row in reader:
		for (k,v) in row.items():
			columns[k].append(v)
ax = pyplot.gca()
hfmt = dates.DateFormatter('%y')
ax.xaxis.set_major_formatter(hfmt)
ax.xaxis.set_major_locator(dates.YearLocator())

for x, y in [(columns['Month'], columns['ACC']), (columns['Month'], columns['Airtel']), (columns['Month'], columns['Asian_Paints'])]:
    dt_x = dates.date2num([datetime.strptime(d, "%Y-%m") for d in x])
    plt.plot(dt_x, y)

ax.set_xlabel('Year from 2005 to 2019')
ax.set_ylabel('Standardized GSV values')
plt.legend(["ACC", "Airtel", "Asian_Paints"])

plt.show()

