import os
import csv

# path to budget file
bugdet_csv = os.path.join("Resources","budget_data.csv")

# path to analysis report file
analysis_file = os.path.join("analysis","analysis_report.txt")

# function that runs analysis
def run_analysis(input_rows, input_length):
    # initialize variables used in iteration and list for monthly changes
    greatest_increase = 0
    greatest_decrease = 0
    changes = []
    net_profit = 0.00

    # iterate through list argument ignoring first month
    for row in range(1, input_length):
        
        #sums net profit
        net_profit = net_profit + float(input_rows[row][1])
        
        # calculates hmonth over month change per iteration and stores in list
        changes.append(float(input_rows[row][1]) - float(input_rows[row-1][1]))

    # finds value for greatest increase and decrease and sets variables
        for row in range(0, len(changes)):
            if float(changes[row]) > greatest_increase:
                greatest_increase = changes[row]
                month_increase = input_rows[row][0]
            
            elif float(changes[row]) < greatest_decrease:
                greatest_decrease = changes[row]
                month_decrease = input_rows[row][0]
    
    # run remaining calculations
    avg_change = sum(changes)/len(changes)

    # create print statements using variables
    print_title = 'Financial Analysis'
    print_spacer = '----------------------------'
    print_months = f"Total Months: {input_length}"
    print_net = f"Total: ${net_profit:.2f}"
    print_change = f"Average Change: ${avg_change:.2f}"
    print_increase = f"Greatest Increase in Profits: {month_increase} (${greatest_increase:.2f})"
    print_decrease = f"Greatest Decrease in Profits: {month_decrease} (${greatest_decrease:.2f})"

    # return list with print statements
    return (print_title, print_spacer, print_months, print_net, print_change, print_increase, print_decrease)

# open budget file and creates list with rows and row count
with open(bugdet_csv, 'r') as input_csv:
    input_reader = csv.reader(input_csv, delimiter=',')
    input_header = next(input_reader)
    input_rows = list(input_reader)
    input_length = len(input_rows)
    
    # pass list of row values to function and set variable for return list
    results = run_analysis(input_rows, input_length)

# open analysis report file, newline parameter to remove carriage
with open(analysis_file, 'w', newline='') as output_file:
    output_writer = csv.writer(output_file, delimiter=',')

    # write each print lines to analysis_report.txt file
    for result in results:
        output_writer.writerow([result])
        
        # print each line to terminal
        print(result)
    
    # removes last line empty line from file to make OCD happy
    # original code from stack overflow:
    # https://stackoverflow.com/questions/53086588/delete-last-and-blank-line-from-file-written-by-csv-writer
    output_file.seek(0, os.SEEK_END)
    output_file.seek(output_file.tell()-2, os.SEEK_SET)
    output_file.truncate()