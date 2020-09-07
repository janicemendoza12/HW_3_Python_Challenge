import os
import csv

#file path
csvpath = os.path.join("Resources", "election_data.csv")

with open (csvpath) as Polling_Data:
    csvreader = csv.reader(Polling_Data, delimiter=",")

#variables
    votes = 0
    vote_count = []
    candidates = []

    for row in csvreader:
        votes = votes + 1
        candidate = row[2]
        if candidate in candidates:
            candidate_index = candidates.index(candidate)
            vote_count[candidate_index] = vote_count[candidate_index] + 1
        else:
            candidates.append(candidate)
            vote_count.append(1)
percentages = []
most_votes = vote_count[0]
most_votes_index = 0
for count in range(len(candidates)):
    vote_percentage = vote_count[count]/votes*100
    percentages.append(vote_percentage)
    if vote_count[count] > most_votes:

        most_votes = vote_count[count]
        most_votes_index = count
        winner = candidates[most_votes_index]
    percentages = [round(i,2) for i in percentages]

print("Election Results:" + "\n")
print(f"Total Votes: {votes}")
for count in range(1, len(candidates)):
    print(f"{candidates[count]}: {percentages[count]}% ({vote_count[count]})")
print(f"Winner: {winner}")



    
    