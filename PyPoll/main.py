import os
import csv

# path to budget file
election_csv = os.path.join("Resources","election_data.csv")

# path to analysis report file
analysis_file = os.path.join("analysis","analysis_report.txt")

# function to dynamically create list of ballot results template
def ballot_results_template(input_rows, input_length):
    # initialize list variables
    candidate_list = []
    results_template = []

    # find distinct candidate names
    for row in range(0, input_length):
        if input_rows[row][2] not in candidate_list:
            candidate_list.append(input_rows[row][2])

    # create ballot results template list with initialized vote count
    for candidate in candidate_list:
        results_template.append([candidate, 0, ''])

    # return ballot results template list
    return results_template

# function that runs analysis
def run_analysis(input_rows, input_length):
    # # call function to dynamically create a unique candidate list
    ballot_results = ballot_results_template(input_rows, input_length)

    # count votes from input list and store in ballot results template list
    for row in range(0, input_length):
        for candidate in range(0, len(ballot_results)): 
            if ballot_results[candidate][0] == input_rows[row][2]:
                ballot_results[candidate][1] = ballot_results[candidate][1] + 1

    # find winner and mark in results
    for row in range(0, len(ballot_results)):
        if ballot_results[row][1] > ballot_results[row-1][1]:
            ballot_results[row][2] = 'Winner'
            ballot_results[row-1][2] = ''
    
    # return ballot results list
    return (ballot_results)

# open budget file and creates list with rows and row count
with open(election_csv, 'r') as input_csv:
    input_reader = csv.reader(input_csv, delimiter=',')
    input_header = next(input_reader)
    input_rows = list(input_reader)
    input_length = len(input_rows)

    # pass list of row values to function and set variable for return list
    results = run_analysis(input_rows, input_length)

# open analysis report file, newline parameter to remove carriage
with open(analysis_file, 'w', newline='') as output_file:
    output_writer = csv.writer(output_file, delimiter=',')

    # set print statements
    title = 'Election Results'
    spacer = '----------------------------'

    # write/print title and spacer
    output_writer.writerow([title])
    output_writer.writerow([spacer])
    print(title)
    print(spacer)

    # write/print total # of votes
    output_writer.writerow([f'Total Votes: {input_length}'])
    print(f'Total Votes: {input_length}')

    # write/print spacer
    output_writer.writerow([spacer])
    print(spacer)

    # dynamically write/print results
    for row in range(0, len(results)):
        output_writer.writerow([f'{results[row][0]}: {(results[row][1]/input_length):.3%} ({results[row][1]})'])
        print(f'{results[row][0]}: {(results[row][1]/input_length):.3%} ({results[row][1]})')

    # write/print spacer
    output_writer.writerow([spacer])
    print(spacer)

    # write/print winner - "KHHHHHHHHHAAAAAAAAAAAAAAAAAAAAAAAAAANNNNNNNNNNNNNNNNNNN!!!!"
    for row in range(0, len(results)):
        if results[row][2] == 'Winner':
            output_writer.writerow([f'Winner: {results[row][0]}'])
            print(f'Winner: {results[row][0]}')
        
    # write/print final spacer
    output_writer.writerow([spacer])
    print(spacer)
    
    # removes last line empty line from file to make OCD happy
    # original code from stack overflow:
    # https://stackoverflow.com/questions/53086588/delete-last-and-blank-line-from-file-written-by-csv-writer
    output_file.seek(0, os.SEEK_END)
    output_file.seek(output_file.tell()-2, os.SEEK_SET)
    output_file.truncate()