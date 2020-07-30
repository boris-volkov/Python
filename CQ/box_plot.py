import csv
import matplotlib.pyplot as plt
plt.rcParams['axes.facecolor'] = '#772953'

cyan        = '\u001b[96m'
yellow      = '\u001b[93m'
green       = '\u001b[92m'

scores = {}

def print_high_scores(x: dict):
    print(yellow + ' ' *10 + 'HIGH SCORES')
    for key, value in reversed(sorted(x.items(), key=lambda item: item[1])[-10:]):
        print(green + f'{key:20s}'  + cyan + '    :    '  +  yellow + str(value))

with open('records.csv') as records:
    reader = csv.DictReader(records)
    for row in reader:
        if (row['time'] == '300' and row['age'] != '') and (str.upper(row['age']) not in scores or int(scores[str.upper(row['age'])]) < int(row['level'])):
            scores.update({str.upper(row['age']) : int(row ['level'])})

box_plot_data = scores.values()
plt.figure(figsize=(11,8))
plt.suptitle("score distribution of everyone who has played")
plt.boxplot(box_plot_data, patch_artist=True, vert = False,
        labels = ['box plot'], manage_ticks = True,
        boxprops=dict(color = 'yellow'),
        whiskerprops=dict(color = 'yellow'),
        flierprops=dict(color = 'yellow', markeredgecolor='yellow'),
        capprops=dict(color = 'yellow'))
plt.show()

print_high_scores(scores)
