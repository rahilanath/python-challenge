import os
import csv

# path to budget file
bugdet_csv = os.path.join("Resources","budget_data.csv")

# path to analysis report file
analysis_file = os.path.join("analysis","analysis_report.txt")

# function that runs analysis
def run_analysis(input_list, input_rows):
    # initialize variables used in iteration and list for monthly changes
    profit = 0.00
    loss = 0.00
    increase = 0
    decrease = 0
    changes = []

    # iterate through list argument
    for row in range(0, input_rows):

        # sums profit month over month
        if float(input_list[row][1]) > 0:
            profit = profit + float(input_list[row][1])
        
        # sums loss month over month
        elif float(input_list[row][1]) < 0:
            loss = loss + float(input_list[row][1])
        
        # calculates change from previous month per iteration and stores in changes list
        if row > 0:
            changes.append(float(input_list[row][1]) - float(input_list[row-1][1]))

            # updates value for increase and decrease iteration variables
            if float(input_list[row][1]) > float(input_list[increase][1]):
                increase = row
                incmonth = input_list[row][0]
            
            elif float(input_list[row][1]) < float(input_list[decrease][1]):
                decrease = row
                decmonth = input_list[row][0]
    
    # run calculations and set variables for print statements
    net = profit + loss
    avgchange = sum(changes)/len(changes)
    greatest_increase = float(input_list[increase][1])
    greatest_decrease = float(input_list[decrease][1])
    month_increase = input_list[increase][0]
    month_decrease = input_list[decrease][0]

    # create print statements
    title = 'Financial Analysis'
    spacer = '----------------------------'
    total_months = f"Total Months: {input_length}"
    net = f"Total: ${net:.2f}"
    avg_change = f"Average Change: ${avgchange:.2f}"
    month_increase = f"Greatest Increase in Profits: {month_increase} (${greatest_increase:.2f})"
    month_decrease = f"Greatest Decrease in Profits: {month_decrease} (${greatest_decrease:.2f})"

    # return list with print statements
    return (title, spacer, total_months, net, avg_change, month_increase, month_decrease)

# open budget file and creates list with rows and row count
with open(bugdet_csv, 'r') as input_csv:
    input_reader = csv.reader(input_csv, delimiter=',')
    input_header = next(input_reader)
    input_rows = list(input_reader)
    input_length = len(input_rows)
    
    # pass list of row values to function and set variable for return list
    results = run_analysis(input_rows, input_length)

# open analysis report file with newline parameter to remove carriage
with open(analysis_file, 'w', newline='') as output_file:
    output_writer = csv.writer(output_file, delimiter=',')

    # write each print lines to analysis_report.txt file
    for result in results:
        output_writer.writerow([result])
        
        # print each line to terminal
        print(result)