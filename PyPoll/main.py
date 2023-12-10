import os
import csv

poll_data = r'C:\Users\emily\OneDrive\Desktop\Starter_Code\python-challenge\PyPoll\Resources\election_data.csv'

# Initialize variables for analysis

total_votes = 0
votes_per_candidate = 0

# open the CSV file

with open(poll_data, 'r') as csv_file:
    csv_reader = csv.DictReader (csv_file)

    next(csv_reader)

    # Interate through the rows in the CSV file
    for row in csv_reader:

        total_votes = total_votes + 1
        
        

    print("Election Results")
    print("-----------------------")
    print(f"Total Votes: {total_votes}")
   

