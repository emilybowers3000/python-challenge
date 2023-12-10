import os
import csv

budget_data = r'C:\Users\emily\OneDrive\Desktop\Starter_Code\python-challenge\PyBank\Resources\budget_data.csv'

# Initialize variables for analysis
total_months = 0
net_total = 0


# Open the CSV file
with open(budget_data, 'r') as csv_file:
    # Create a CSV DictReader object
    csv_reader = csv.DictReader(csv_file)

    # Iterate through the rows in the CSV file
    for row in csv_reader:
   
        # Increment the total number of months
        total_months = total_months + 1

        # Convert "Profit/Losses" to an integer
        profit_loss = int(row['Profit/Losses'])

        net_total = profit_loss + net_total


    # Print the financial analysis results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")    

