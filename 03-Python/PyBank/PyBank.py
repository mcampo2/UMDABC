# PyBank - Michael Campo

import csv
import os

# * In this challenge, you are tasked with creating a Python script for
#   analyzing the financial records of your company. You will give a set of
#   financial data called budget_data.csv. The dataset is composed of two
#   columns: Date and Profit/Losses. (Thankfully, your company has rather lax
#   standards for accounting so the records are simple.)

# open budget_data.csv
csvpath = os.path.join("Resources", "budget_data.csv")
csvfile = open(csvpath)
csvreader = csv.reader(csvfile)
# read the header from budget_data.csv
header = next(csvreader)
# print(str(header)) # ['Date', 'Profit/Losses']



# * Your task is to create a Python script that analyzes the records to
#   calculate each of the following:
#   - The total number of months included in the dataset
#   - The net total amount of "Profit/Losses" over the entire period
#   - The average of the changes in "Profit/Losses" over the entire period
#   - The greatest increase in profits (date and amount) over the entire period
#   - The greatest decrease in losses (date and amount) over the entire period

# read the first row of data from budget_data.csv
totalMonths = 1
total = next(csvreader)
greatestIncrease = total
greatestDecrease = total
total = int(total[1])
previous = total
change = 0

# read the rest of the data from budget_data.csv
for row in csvreader:
    # print(row)
    change += int(row[1]) - previous
    totalMonths += 1
    total += int(row[1])
    if int(row[1]) > int(greatestIncrease[1]): greatestIncrease = row
    if int(row[1]) < int(greatestDecrease[1]): greatestDecrease = row
    previous = int(row[1])
    
# we are now done with budget_data.csv and the file can be closed
csvfile.close()



# * As an example, your analysis should look similar to the one below:
#
#   Financial Analysis
#   ----------------------------
#   Total Months: 86
#   Total: $38382578
#   Average  Change: $-2315.12
#   Greatest Increase in Profits: Feb-2012 ($1926159)
#   Greatest Decrease in Profits: Sep-2013 ($-2196167)
#

# print the data
print("Financial Analysis")
print("-"*18)
print("Total Months: " + str(totalMonths))
print("Total: $" + str(total))
print("Average Change: $" + str(change*100//(totalMonths-1)/100))
print("Greatest Increase in Profits: " + greatestIncrease[0] \
      + " (" + str(greatestIncrease[1]) + ")")
print("Greatest Decrease in Profits: "+ greatestDecrease[0] \
      + " ($" + str(greatestDecrease[1]) + ")")

# * In addition, your final script should both print the analysis to the
#   terminal and export a text file with the results.

# print the data again, but this time into a file
output = open("pybank.txt", "w")
output.write("Financial Analysis\r")
output.write("-"*18 + "\r")
output.write("Total Months: " + str(totalMonths) + "\r")
output.write("Total: $" + str(total) + "\r")
output.write("Average Change: $" + str(change*100//(totalMonths-1)/100) + "\r")
output.write("Greatest Increase in Profits: " + greatestIncrease[0] \
      + " (" + str(greatestIncrease[1]) + ")\r")
output.write("Greatest Decrease in Profits: "+ greatestDecrease[0] \
      + " ($" + str(greatestDecrease[1]) + ")\r")
output.close()