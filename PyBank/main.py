import os
import csv

# path to budget file
bugdet_csv = os.path.join("Resources","budget_data.csv")

with open(bugdet_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    total_months = len(list(csvreader)))