import os
import csv

# Set the file path
file_path = os.path.join("PyPoll", "Resources", "election_data.csv")

# Initialize variables to store vote counts and candidate names
total_votes = 0
candidates = {}

# Open the CSV file and read the data
with open(file_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    # Skip the header row
    next(csv_reader)
    
    # Loop through each row in the CSV file
    for row in csv_reader:
        # Increment the total vote count
        total_votes += 1
        
        # Get the candidate name from the current row
        candidate_name = row[2]
        
        # If the candidate is not already in the dictionary, add them with a vote count of 1
        if candidate_name not in candidates:
            candidates[candidate_name] = 1
        # If the candidate is already in the dictionary, increment their vote count
        else:
            candidates[candidate_name] += 1

# Print the results to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

# Loop through the candidate dictionary and calculate their vote percentage and print the results
winner = ""
winner_vote_count = 0
for candidate in candidates:
    vote_count = candidates[candidate]
    vote_percentage = vote_count / total_votes * 100
    print(f"{candidate}: {vote_percentage:.3f}% ({vote_count})")
    
    # Check if this candidate has more votes than the current winner
    if vote_count > winner_vote_count:
        winner = candidate
        winner_vote_count = vote_count

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")