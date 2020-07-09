import os
import csv

# path to budget file
bugdet_csv = os.path.join("Resources","budget_data.csv")

# function that runs analysis
def run_analysis(csv_list, csv_rows):
    # initialize variables
    profit = 0.00
    loss = 0.00
    changes = []
    increase = 0
    decrease = 0

    # iteration for list created from csv file
    for row in range(0, csv_rows):

        # sums profit month over month
        if float(csv_list[row][1]) > 0:
            profit = profit + float(csv_list[row][1])
        
        # sums loss month over month
        elif float(csv_list[row][1]) < 0:
            loss = loss + float(csv_list[row][1])
        
        # calculates change month over month
        if row > 0:
            changes.append(float(csv_list[row][1]) - float(csv_list[row-1][1]))

            # updates greatest increase and decrease
            if float(csv_list[row][1]) > float(csv_list[increase][1]):
                increase = row
            
            elif float(csv_list[row][1]) < float(csv_list[decrease][1]):
                decrease = row
    
    net = profit + loss
    avgchange = sum(changes)/len(changes)

    return (net, avgchange, increase, decrease)

# open .csv file
with open(bugdet_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    csvrows = list(csvreader)
    numrows = len(csvrows)
    
    # call function and assign values to list
    results = run_analysis(csvrows, numrows)

    # assign variables to results
    net = int(results[0])
    avgchange = float(results[1])
    incmonth = csvrows[results[2]][0]
    increase = csvrows[results[2]][1]
    decmonth = csvrows[results[3]][0]
    decrease = csvrows[results[3]][1]

    print(f"{results[0]:.2f}")
    
    print('Financial Analysis')
    print('----------------------------')
    print(f"Total Months: {numrows}")
    print(f"Total: ${net}")
    print(f"Average Change: ${avgchange:.2f}")
    print(f"Greatest Increase in Profits: {incmonth} ({increase})")
    print(f"Greatest Decrease in Profits: {decmonth} ({decrease})")