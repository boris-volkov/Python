import csv
import sys

with open('records.csv') as records:
    reader = csv.reader(records)
    next(reader)
    sortedlist = sorted(reader, key = lambda row: int(row[1]), reverse = True)
    for row in sortedlist[:3]:
        print(row[:-1])


