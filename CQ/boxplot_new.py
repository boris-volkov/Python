import time
import csv
import matplotlib
import matplotlib.pyplot as plt
from datetime import datetime
plt.rcParams['axes.facecolor'] = '#772953'
plt.rcParams['figure.figsize'] = 11,8

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
        if (row['time'] == '300' and row['age'] != '') and (str.upper(row['age']) not in scores or int(scores[str.upper(row['age'])]) < int(row['level'])):
            scores.update({str.upper(row['age']) : int(row ['level'])})
    latest_player = row['age']

with open('records.csv') as records_2:    
    second_reader = csv.DictReader(records_2)
    for row in second_reader:
        if (str.upper(row['age']) == str.upper(latest_player)):
            player_history.append((row['date'], row['level']))


box_plot_data = scores.values()
'''
print(player_history)

dates = []
scores = []

for x,y in player_history:
    dates += time.strptime(x, "%a %b %d %H:%M:%S %Y")
    scores += y

print(dates)

dates_num = matplotlib.dates.date2num(dates)
'''

#print(player_history)
num_games = []
for i in range(len(player_history)):
    num_games.append(i + 1)
y = []
for x in player_history:
    y.append(int(x[1]))
def history():
    plt.suptitle('Everyone\'s scores' + ' '*80 + ' Your progression')
    plt.subplot(122)
    plt.plot(num_games, y)


#print(num_games)
#print(y)
'''
def boxplot():
    plt.subplot(121)
    plt.suptitle("score distribution of everyone who has played(left): and your history(right)")
    plt.boxplot(box_plot_data, patch_artist=True, vert = True,
        labels = ['box plot'], manage_ticks = True,
        boxprops=dict(color = 'yellow'),
        whiskerprops=dict(color = 'yellow'),
        flierprops=dict(color = 'yellow', markeredgecolor='yellow'),
        capprops=dict(color = 'yellow'))
'''

def histogram():
    plt.subplot(121)
    plt.hist(box_plot_data, 20, facecolor = 'yellow')

history()
histogram()
#boxplot()
#plt.axis('equal')
plt.show()

print_high_scores(scores)
