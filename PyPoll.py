#The data we need to retrieve.
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote
#add our dependencies
import csv
import os
#
#Assign a variable for the file to load and the path.
file_to_load= os.path.join("Resources","election_results.csv")
#create a filename variable to a direcct or indirect path to the file
file_to_save = os.path.join("analysis","election_analysis.txt")
#
#
#1.initialize a total vote ocunter
total_votes = 0
#candidate options and canidate votes
candidate_options =[]
#declare the empty dictionary canidate votes
candidate_votes ={}
#winning candidate and winning count tracker
winning_candidate =""
winning_count =0
winning_percentage =0 
#
#Open the election results and read the file
with open(file_to_load) as election_data:
    #read the file object with the reader function. 
    file_reader=csv.reader(election_data)
    #pread header row
    headers= next(file_reader)
    #
    #print each row in the csv file
    for row in file_reader:
        #2. Add to the total vote count
        total_votes += 1
        #print the candidate name from each row.
        candidate_name = row[2] 
        #if candidate does not match any existing candidate
        if candidate_name not in candidate_options:
        # add the candidate name to the candidate list
            candidate_options.append(candidate_name)
            #begin tracking that candidates vote count
            candidate_votes[candidate_name]=0
        #add a vote to that ccanidates count
        candidate_votes[candidate_name] +=1
#determine the percentage of votes for each candidate by looping throuhg the counts
#1 iterate through the candidate list
for candidate_name in candidate_votes:
    #2 Retrieve vote count of a candidate
    votes= candidate_votes[candidate_name]
    #3 calculate the percentage of votes
    vote_percentage = round((float(votes)/ float(total_votes)*100),2) 
    #4 print the candidate name and percentage of votes
    print(f"{candidate_name}: receved {vote_percentage}% of the vote.")   
 



