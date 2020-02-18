# PyPoll - Michael Campo

import csv
import os

# * In this challenge, you are tasked with helping a small, rural town
#   modernize its vote-counting process. (Up until now, Uncle Cleetus had been
#   trustfully tallying them one-by-one, but unfortunately, his concentration
#   isn't what it used to be.)

# * You will be give a set of poll data called election_data.csv. The dataset
#   is composed of three columns: Voter ID, County, and Candidate. Your task is
#   to create a Python script that analyzes the votes and calculates each of
#   the following:
#   - The total number of votes cast
#   - A complete list of candidates who received votes
#   - The percentage of votes each candidate won
#   - The total number of votes each candidate won
#   - The winner of the election based on popular vote.

# open election_data.csv
csvpath = os.path.join("Resources", "election_data.csv")
csvfile = open(csvpath)
csvreader = csv.reader(csvfile)
# read the header from election_data.csv
header = next(csvreader)
# print(str(header)) # ['Voter ID', 'County', 'Candidate']

# store the votes in a dictionary
votes = {}
for row in csvreader:
    # read the row into variables to better readability
    voterID = row[0]
    county = row[1]
    candidate = row[2]
    # if the candidate is in the dictionary, add a vote
    if candidate in votes:
        votes[candidate] += 1
    else: # this is a new candidate, set their votes to "1"
        votes[candidate] = 1

# we are now done with election_data.csv
csvfile.close()

# calculate total votes
total = 0
for candidate in votes:
    total += votes[candidate]



# * As an example, your analysis should look similar to the one below:
#
#   Election Results
#   -------------------------
#   Total Votes: 3521001
#   -------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan
#   -------------------------
#

# print the results
print("Election Results")
print("-"*16)
print("Total Votes: " + str(total))
print("-"*16)
# print each candidate's statistics
for candidate in votes:
    print(candidate + ": " + "%0.3f"% (votes[candidate]*100.0/total) \
          + "% (" + str(votes[candidate]) + ")")
print("-"*16)
# print the winner of the election
print("Winner: " + max(votes, key=votes.get))
print("-"*16)




# * In addition, your final script should both print the analysis to the
#   terminal and export a text file with the results.

# print the results again, this time to a file
output = open("pypoll.txt", "w")
output.write("Election Results\r")
output.write("-"*16 + "\r")
output.write("Total Votes: " + str(total) + "\r")
output.write("-"*16 + "\r")
for candidate in votes:
    output.write(candidate + ": " + "%0.3f"% (votes[candidate]*100.0/total) \
          + "% (" + str(votes[candidate]) + ")\r")
output.write("-"*16 + "\r")
output.write("Winner: " + max(votes, key=votes.get) + "\r")
output.write("-"*16 + "\r")
output.close()