import os
import csv

budget_data = r'C:\Users\emily\OneDrive\Desktop\python-challenge\PyBank\Resources\budget_data.csv'
output_file = "financial_analysis.txt"

# Initialize variables for analysis
total_months = 0
net_total = 0
previous_profit_loss = 0
profit_changes = []
months = []

# Open the CSV file
with open(budget_data, 'r') as csv_file:
    # Create a CSV DictReader object
    csv_reader = csv.DictReader(csv_file)

    # Iterate through the rows in the CSV file
    for row in csv_reader:
        # Increment the total number of months
        total_months += 1

        # Convert "Profit/Losses" to an integer
        profit_loss = int(row['Profit/Losses'])
        net_total += profit_loss

        # Track profit changes
        if total_months > 1:
            profit_change = profit_loss - previous_profit_loss
            profit_changes.append(profit_change)
            months.append(row['Date'])

        # Update previous profit/loss for next iteration
        previous_profit_loss = profit_loss

# Calculate average change
average_change = sum(profit_changes) / (total_months - 1)

# Find greatest increase and decrease in profits
greatest_increase = max(profit_changes)
greatest_decrease = min(profit_changes)

# Get the index of the greatest increase and decrease to retrieve the corresponding month
greatest_increase_index = profit_changes.index(greatest_increase)
greatest_decrease_index = profit_changes.index(greatest_decrease)

# Get the corresponding months for greatest increase and decrease
greatest_increase_month = months[greatest_increase_index]
greatest_decrease_month = months[greatest_decrease_index]

# Print the financial analysis results

analysis_results = f"""Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${net_total}
Average Change: ${average_change:.2f}
Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})
Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})
"""

# Print the analysis results to the terminal
print(analysis_results)

# Export the analysis results to a text file
with open(output_file, "w") as txt_file:
    txt_file.write(analysis_results)

print("Analysis results have been exported to financial_analysis.txt.")