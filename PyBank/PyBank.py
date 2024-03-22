#import the necessary libraries for reading csv files and writing to a text file
import os
import csv
with open('/Users/morgansmith/Desktop/Python-Challenge/PyBank/Resources/budget_data.csv') as csvfile:
    csvreader = csv.reader(csvfile)
    rows = []
    for row in csvreader:
        rows.append(row)
#print the rows
for row in rows:
    print(row)

#now calculate the total number of months included in the dataset
    total_months = len(rows) - 1
print("Financial Analysis")
print("----------------------------")
print("Total Months:", total_months)

#calculate the net total amount of "Profit/Losses" over the entire period
Total_sales = 0
count = 1
sales = 0
first_sale = 0
last_sale = 0
for row in rows:
    month = row[0]
    if count > 1:
        sales = int(row[1])
    if count == 2:
        first_sale = sales
    if count == 87:
        last_sale = sales
    count = count + 1
    Total_sales = Total_sales + sales
print("Total: $", Total_sales)

#calculate the changes in "Profit/Losses" over the entire period, and then the average of those changes
changes = last_sale - first_sale
average_change = changes / (total_months - 1)
print("Average Change: $", average_change)

#now calculate the greatest increase in profits (date and amount) over the entire period, and then average of those changes
greatest_increase = 0
greatest_increase_month = ""
for row in rows:
    month = row[0]
    profit_loss = int(row[1])
    if profit_loss > 0:
        if profit_loss > greatest_increase:
            greatest_increase = profit_loss
            greatest_increase_month = month
print("Greatest Increase in Profits:", greatest_increase_month, f"(${greatest_increase})")









#PyPoll section
#import the necessary libraries for reading csv files and writing to a text file
import os
import csv
import os
import csv
import os
import csv
with open('/Users/morgansmith/Desktop/Python-Challenge/PyPoll/Resources/election_data.csv') as csvfile:
    csvreader = csv.reader(csvfile)
#calculate the total number of votes cast
    rows = []
    for row in csvreader:
        rows.append(row)
        total_votes = len(rows) - 1
    print("Election Results")
    print("----------------------------")
    print("Total Votes:", total_votes)
#import the necessary libraries for reading csv files and writing to a text file
with open('/Users/morgansmith/Desktop/Python-Challenge/PyBank/Resources/budget_data.csv') as csvfile:
    csvreader = csv.reader(csvfile)
    rows = []
    for row in csvreader:
        rows.append(row)
    #print the rows
    for row in rows:
        print(row)

    #now calculate the total number of months included in the dataset
    total_months = len(rows) - 1
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months:", total_months)

    #calculate the net total amount of "Profit/Losses" over the entire period
    Total_sales = 0
    count = 1
    sales = 0
    first_sale = 0
    last_sale = 0
    for row in rows:
        month = row[0]
        if count > 1:
            sales = int(row[1])
        if count == 2:
            first_sale = sales
        if count == 87:
            last_sale = sales
        count = count + 1
        Total_sales = Total_sales + sales
    print("Total: $", Total_sales)

    #calculate the changes in "Profit/Losses" over the entire period, and then the average of those changes
    changes = last_sale - first_sale
    average_change = changes / (total_months - 1)
    print("Average Change: $", average_change)


#now calculate the greatest increase in profits (date and amount) over the entire period, and then average of those changes
    greatest_increase = 0
    greatest_increase_month = ""
    for row in rows:
        month = row[0]
        profit_loss = int(row[1])
        if profit_loss > 0:
            if profit_loss > greatest_increase:
                greatest_increase = profit_loss
                greatest_increase_month = month
    print("Greatest Increase in Profits:", greatest_increase_month, f"(${greatest_increase})")

# now calculate the greatest decrease in profits (date and amount) over the entire period
    greatest_decrease = 0
    greatest_decrease_month = ""
    for row in rows:
        month = row[0]
        profit_loss = int(row[1])
        if profit_loss < 0:
            if profit_loss < greatest_decrease:
                greatest_decrease = profit_loss
                greatest_decrease_month = month
    print("Greatest Decrease in Profits:", greatest_decrease_month, f"(${greatest_decrease})")