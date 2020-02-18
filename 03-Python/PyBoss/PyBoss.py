# PyBoss - Michael Campo

import csv
import os

# In this challenge, you get to be the boss. You oversee hundreds of employees
# across the country developing Tuna 2.0, a world-changing snack food based on
# canned tuna fish. Alas, being the boss isn't all fun, games, and self-
# adulation. The company recently decided to purchase a new HR system, and
# unfortunately for you, the new system requires employee records be stored
# completely differently.

# Your task is to help bridge the gap by creating a Python script able to
# convert your employee records to the required format. Your script will need
# to do the following:

# * Import the employee_data.csv file, which currently holds employee records
#   like the below:
#
#   Emp ID,Name,DOB,SSN,State
#   214,Sarah Simpson,1985-12-04,282-01-8166,Florida
#   15,Samantha Lara,1993-09-08,848-80-7526,Colorado
#   411,Stacy Charles,1957-12-20,658-75-8526,Pennsylvania
#

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

# open employee_data.csv
csvpath = os.path.join("employee_data.csv")
csvfile = open(csvpath)
csvreader = csv.reader(csvfile)
# read the header from employee_data.csv
header = next(csvreader)
# print(header) # ['Emp ID', 'Name', 'DOB', 'SSN', 'State']



# * Then convert and export the data to use the following format instead:
#
#   Emp ID,First Name,Last Name,DOB,SSN,State
#   214,Sarah,Simpson,12/04/1985,***-**-8166,FL
#   15,Samantha,Lara,09/08/1993,***-**-7526,CO
#   411,Stacy,Charles,12/20/1957,***-**-8526,PA
#

# create lists to store the data from employee_data.csv in its new format
header = ["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"]
empIDs = []
firstNames = []
lastNames = []
DOBs = []
SSNs = []
states = []

# read employee_data.csv into the newly created lists
for row in csvreader:
    empIDs.append(row[0])
    firstNames.append(row[1].split(" ")[0])
    lastNames.append(row[1].split(" ")[1])
    DOBs.append(row[2].split("-")[1] + "/" + row[2].split("-")[2] \
                + "/" + row[2].split("-")[0])
    SSNs.append("***-**-" + row[3].split("-")[2])
    states.append(us_state_abbrev[row[4]])

# we are done with employee_data.csv and can close the file
csvfile.close()

# combine the lists into a table using the builtin zip function
converted = zip(empIDs, firstNames, lastNames, DOBs, SSNs, states)

# write the table into a file
output = open("PyBoss.csv", "w", newline="")
csvout = csv.writer(output)
csvout.writerow(header)
csvout.writerows(converted)
output.close()

# * In summary, the required conversions are as follows:
#   - The Name column should be split into separate First Name and Last Name
#     columns.
#   - The DOB data should be re-written into MM/DD/YYYY format.
#   - The SSN data should be re-written such that the first five numbers are
#     hidden from view.
#   - The State data should be re-written as simple two-letter abbreviations.

# * Special Hint: You may find this link to be helpful—Python Dictionary for
#   State Abbreviations. [https://gist.github.com/afhaque/
#   29f0f4f37463c447770517a6c17d08f5]
