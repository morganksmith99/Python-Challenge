#PyPoll section
#import the necessary libraries for reading csv files and writing to a text file
import os
import csv
with open('/Users/morgansmith/Desktop/Python-Challenge/PyPoll/Resources/election_data.csv') as csvfile:
    csvreader = csv.reader(csvfile)
    #calculate total number of votes cast
    rows = []
    for row in csvreader:
        rows.append(row)
        total_votes = len(rows) - 1
    print("Election Results")
    print("----------------------------")
    print("Total Votes:", total_votes)
# calculate A complete list of candidates who received votes
    candidate_list = []
    for row in rows:
        candidate = row[2]
        if candidate not in candidate_list:
            candidate_list.append(candidate)
    print("Candidates who received votes:", candidate_list)
# calculate The percentage of votes each candidate won
    candidate_votes = {}
    for candidate in candidate_list:
        votes = 0
        for row in rows:
            if row[2] == candidate:
                votes = votes + 1
        candidate_votes[candidate] = votes
    print("Votes per candidate:", candidate_votes)

# calculate the percentage of votes each candidate won (make sure percentages are actual percentages with the % sign)
    for candidate in candidate_list:
        votes = candidate_votes[candidate]
        percentage = (votes / total_votes) * 100
        print(candidate, ":", "{:.2f}".format(percentage), "%")
    
#calculate the winner of the election based on popular vote
    winner = ""
    winning_votes = 0
    for candidate in candidate_list:
        votes = candidate_votes[candidate]
        if votes > winning_votes:
            winner = candidate
            winning_votes = votes
    print("Winner:", winner)

