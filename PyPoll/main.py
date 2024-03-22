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


    

