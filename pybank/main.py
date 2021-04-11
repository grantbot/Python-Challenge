#pybank

import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')
output_path = os.path.join('Analysis', "PyBank_Analysis.txt")

# initialize variables

total_months = 0
total_net = 0
total_change = 0
month_start = 0
month_result = []
monthly_profit_change = []

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
     
    header_row = next(csvreader)
    first_row = next(csvreader)
    previous_month = int(first_row[1])
    total_months += 1
    total_net += int(first_row[1])

    for row in csvreader:
       
        # count the number of rows to determine the number of months
        total_months += 1
        # total up all values in Profit/Losses 
        total_net += int(row[1])
        # find the average change for Profit/Losses 
        month_end = int(row[1])
        monthly_profit_change = month_end - previous_month
        previous_month = month_end
        # store monthly profit change in list
        month_result.append(monthly_profit_change)
        
total_month_result = sum(month_result)
avg = total_month_result/total_months

# The greatest increase in profits (date and amount) over the entire period     
greatest_profit = max(month_result)
greatest_loss = min(month_result)

# create summary table 
output = (
    f"\n"
    f"Financial Analysis\n"
    f"-------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: {total_net}\n"
    f"Average Change: {avg}\n"
    f"Greatest Increase in Profits: {greatest_profit}\n"
    f"Greatest Decrease in Profits: {greatest_loss}\n"
)
#print to terminal
print(output)

# save results to text file 
with open(output_path, "w") as txt_file:
    txt_file.write(output)






