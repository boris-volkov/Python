import time
import csv
import matplotlib
import matplotlib.pyplot as plt
from datetime import datetime
plt.rcParams['axes.facecolor'] = '#772953'
plt.rcParams['figure.figsize'] = 11,8
plt.rcParams.update({'font.size' : 7})

cyan        = '\u001b[96m'
yellow      = '\u001b[93m'
green       = '\u001b[92m'

scores = {}
player_history = []

def print_high_scores(x: dict):
    print(yellow + ' ' *10 + 'HIGH SCORES')
    for key, value in reversed(sorted(x.items(), key=lambda item: item[1])[-10:]):
        print(green + f'{key:20s}'  + cyan + '    :    '  +  yellow + str(value))

with open('records.csv') as records:
    reader = csv.DictReader(records)
    for row in reader:
        if (row['time'] == '300' and row['age'] != ''):
            scores.update({str.upper(row['age']) : int(row ['level'])})
    latest_player = row['age']

box_plot_data = scores.values()

with open('records.csv') as records_2:    
    second_reader = csv.DictReader(records_2)
    for row in second_reader:
        if (str.upper(row['age']) == str.upper(latest_player)):
            player_history.append((row['date'], row['level']))

dates = []
d_scores = []

for record in player_history:
    struct = time.strptime(record[0], "%a %b %d %H:%M:%S %Y")
    dt = datetime.fromtimestamp(time.mktime(struct))
    dates.append(dt)
    d_scores.append(int(record[1]))

bottom_limit = max(0, min(d_scores) - 100) 
top_limit = max(d_scores) + 30

def time_plot():
    plt.suptitle('Everyone\'s scores' + ' '*120 + ' Your progression')
    plt.subplot(122)
    plt.plot_date(dates, d_scores, fillstyle = 'bottom', color = 'yellow', linestyle = '--')
    plt.xticks(rotation = 70)
    axes = plt.gca()
    axes.set_ylim(bottom_limit, top_limit)

def histogram():
    plt.subplot(121)
    plt.hist(box_plot_data, 15, facecolor = 'yellow')

time_plot()
histogram()
plt.show()

print_high_scores(scores)
