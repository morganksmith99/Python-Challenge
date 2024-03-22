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

#calculate A complete list of candidates who received votes, The percentage of votes each candidate won and, The total number of votes each candidate won 
#the outcome should look like this:
# -------------------------
#Charles Casper Stockham: 23.049% (85213)
#Diana DeGette: 73.812% (272892)
#Raymon Anthony Doane: 3.139% (11606)
#-------------------------


    

