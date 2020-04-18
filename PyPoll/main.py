# Your task is to create a Python script that analyzes the votes and calculates each of the following:
# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.

# Modules
import os
import csv
import statistics 

# Set path for file

poll_path = os.path.join("Resources","election_data.csv")

# Make a candidate list
candidate_list =[]

# Open csv file
with open(poll_path) as csvfile:
    csvreader = csv.reader(csvfile)

    #Specify CSV delimiter
    csvreader = csv.reader(csvfile, delimiter=',')

    #Skip header
    csv_header = next(csvreader)

    #Loop to find the candidate names
    for row in csvreader:
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
    print(f'List of candidates: {candidate_list}')

# loop to calculate total votes
with open(poll_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvfile)
    Khan_Votes = 0
    Correy_Votes = 0
    Li_Votes = 0
    OTooley_Votes = 0
    for row in csvreader:
        if row[2] == candidate_list[0]:
            Khan_Votes += 1
        elif row[2] == candidate_list[1]:
            Correy_Votes += 1
        elif row[2] == candidate_list[2]:
            Li_Votes += 1
        elif row[2] == candidate_list[3]:
            OTooley_Votes += 1
Total_Votes = Khan_Votes + Correy_Votes + Li_Votes + OTooley_Votes
print(f'Total Votes: {Total_Votes}')

#The percentage of votes each candidate won
Khan_Percent = round((Khan_Votes/Total_Votes)*100,3)
print(f'Khan: {Khan_Percent} {Khan_Votes}')
Correy_Percent = round((Correy_Votes/Total_Votes)*100,3)
print(f'Correy: {Correy_Percent} {Correy_Votes}')
Li_Percent = round((Li_Votes/Total_Votes)*100,3)
print(f'Li: {Li_Percent} {Li_Votes}')
OTooley_Percent = round((OTooley_Votes/Total_Votes)*100,3)
print(f'OTooly: {OTooley_Percent} {OTooley_Votes}')

#Total number of votes each candidate won
# print(Khan_Votes)
# print(Correy_Votes)
# print(Li_Votes)
# print(OTooley_Votes)

#Winner
if Khan_Votes > Correy_Votes and Khan_Votes > Li_Votes and Khan_Votes > OTooley_Votes:
    winner = "Khan"
elif Correy_Votes > Khan_Votes and Correy_Votes > Li_Votes and Correy_Votes > OTooley_Votes:
    winner = "Correy"
elif Li_Votes > Khan_Votes and Li_Votes > Correy_Votes and Correy_Votes > OTooley_Votes:
    winner = "Li"
elif OTooley_Votes > Khan_Votes and OTooley_Votes > Correy_Votes and OTooley_Votes > Li_Votes:
    winner = "OTooley"
print(f'Winner: {winner}')

output_path = 'Election Results.txt'
with open(output_path, 'w', newline ='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["---------------------------------"])
    csvwriter.writerow([f'Total Votes: {Total_Votes}'])
    csvwriter.writerow(["---------------------------------"])
    csvwriter.writerow([f'Khan: {Khan_Percent}% ({Khan_Votes})'])
    csvwriter.writerow([f'Correy: {Correy_Percent}% ({Correy_Votes})'])
    csvwriter.writerow([f'Li: {Li_Percent}% ({Li_Votes})'])
    csvwriter.writerow([f"O'Tooley: {round((OTooley_Votes/Total_Votes)*100,3)}% ({OTooley_Votes})"])
    csvwriter.writerow(["---------------------------------"])
    csvwriter.writerow([f'Winner: {winner}'])
    csvwriter.writerow(["---------------------------------"])