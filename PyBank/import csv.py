import csv

file_path = r'C:\Users\emily\OneDrive\Desktop\Starter_Code\python-challenge\PyBank\Resources\budget_data.csv'
with open(file_path) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(row)