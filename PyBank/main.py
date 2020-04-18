# Create a Python script that analyzes the PyBank records to calculate each of the following:
# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The average of the changes in "Profit/Losses" over the entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period
# Print the analysis to the terminal and export a text file with the results

# Modules
import os
import csv
from statistics import mean

# Set path for file

csvpath = os.path.join("Resources","budget_data.csv")

# Create a variable to store the data files
Profits = []
months = []
month_change = []
running_total = 0

# make calculation for average
def average (numbers):
    total = 0.0
    for number in numbers:
        total += number
    find_average = total/len(numbers)
    return find_average

with open(csvpath) as csvfile:
    # specify CSV delimiter
    csvreader = csv.reader(csvfile, delimiter=',')
    # remove header
    header = next(csvreader)
    first_line = next(csvreader)

    #total profits start at the first numeric profit/loss row that's why there is an index
    running_total += int(first_line[1]) 
    
    # net for profit include first number 
    previous_net = int(first_line[1])

    # adding the first item (date) to a separate list using the index 0 (zero)
    months.append(first_line[0])

    # Loop now that you have the first line information
    for row in csvreader:
        net_change = int(row[1])- previous_net
        previous_net = int(row[1])
        month_change.append(net_change)
        months.append(row[0])
        running_total += int(row[1]) 
    profits_average=mean(month_change)

#Print Total Months to Check Values
total_months = len(months)
print("Total Months:" + " " + str(total_months))

#Print Total Profits & Losses to Check Values
print(f"Total: ${running_total}")

#Print Average Change to Check Values
print(f"Average Change: ${round(profits_average,2)}")

#Print Greatest Increase in Profits & Greatest Decrease in Profits
greatest_increase = max(month_change) 
print("The greatest increase is" + " " + str(greatest_increase))
greatest_decrease = min(month_change) 
print("The greatest decrease is" + " " + str(greatest_decrease))

#Print Index Dates for max and min profits
max_index = month_change.index(greatest_increase)
max_date = months[max_index]
print("The max date is" + " " + str(max_date))
min_index = month_change.index(greatest_decrease)
min_date = months[min_index]
print("The min date is" + " " + str(min_date))

# csv file - Specify the file to write to
output_path = os.path.join("..", "output", "new.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['---------------------------------'])
    csvwriter.writerow(["Total Months:" + " " + str(total_months)])
    csvwriter.writerow([f"Total: ${running_total}"])
    csvwriter.writerow([f"Average Change: ${round(profits_average,2)}"])
    csvwriter.writerow(["Greatest Increase in Profits:" + " " + str(max_date) + " " + str(greatest_increase)])
    csvwriter.writerow(["Greatest Decrease in Profits:" + " " + str(min_date)+ " " + str(greatest_decrease)])

#Export a text file with the results
target = open("pyBank.txt", 'w')
target.write("Financial Analysis\n")
target.write("----------------------------\n")
target.write(f"Total Months:+ " " + str(total_months)\n")
target.write(f"Total:  ${running_total}\n")
target.write(f"Average Change:  ${round(profits_average,2)}\n")
target.write(f"Greatest Increase in Profits:  {max_date} (${greatest_increase})\n")
target.write(f"Greatest Decrease in Losses:  {min_date} (${greatest_decrease})\n")