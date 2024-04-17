import os
import csv

poll_data = r'C:\Users\emily\OneDrive\Desktop\python-challenge\PyPoll\Resources\election_data.csv'
output_file = "election_results.txt"

# Create variables for analysis
total_votes = 0
candidate_votes = {}

# Open the CSV file
with open(poll_data, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    # Iterate through the rows in the CSV file
    for row in csv_reader:
        # Count the total number of votes
        total_votes += 1

        # Extract the candidate name from the row
        candidate_name = row['Candidate']

        # If the candidate is already in the dictionary, increment their vote count
        if candidate_name in candidate_votes:
            candidate_votes[candidate_name] += 1
        # If the candidate is not in the dictionary, add them with an initial vote count of 1
        else:
            candidate_votes[candidate_name] = 1

# Print the election results
print("Election Results")
print("-----------------------")
print(f"Total Votes: {total_votes}")
print("-----------------------")

# Create variables to find the winner
winner_votes = 0
winner = ""

# Iterate through the dictionary of candidate votes
for candidate, votes in candidate_votes.items():
    # Calculate the percentage of votes each candidate won
    percentage = (votes / total_votes) * 100
    # Print the candidate's name, percentage of votes, and total votes
    print(f"{candidate}: {percentage:.3f}% ({votes})")
    
    # Check if the candidate has more votes than the current winner
    if votes > winner_votes:
        winner_votes = votes
        winner = candidate

print("-----------------------")
print(f"Winner: {winner}")
print("-----------------------")

# Generate the analysis results
analysis_results = "Election Results\n" + "-" * 25 + "\n"
analysis_results += f"Total Votes: {total_votes}\n" + "-" * 25 + "\n"
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    analysis_results += f"{candidate}: {percentage:.3f}% ({votes})\n"
analysis_results += "-" * 25 + "\n"
analysis_results += f"Winner: {winner}\n"
analysis_results += "-" * 25

# Export the analysis results to a text file
with open(output_file, "w") as txt_file:
    txt_file.write(analysis_results)

print(f"Analysis results have been exported to {output_file}.")