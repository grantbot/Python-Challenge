import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')
output_path = os.path.join('Analysis', "PyPoll_Analysis.txt")

#initialize variables 
total_votes = 0
candidates = []
candidates_result = [] 

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    header_row = next(csvreader)

    for row in csvreader:
        # Total up all the votes 
        total_votes += 1
        # Find the total votes each candidate won 
        

        
    






# create summary table 
output = (
    f"\n"
    f"Election Results\n"
    f"------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"------------------------\n"
    f"candidates {candidates}"

)
#print to terminal
print(output)

# save results to text file 
with open(output_path, "w") as txt_file:
    txt_file.write(output)