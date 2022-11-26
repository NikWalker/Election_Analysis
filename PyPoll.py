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
#Assign a variable to load a file from a path
file_to_load= os.path.join("Resources","election_results.csv")
#Assign a variable to save a file from a path
file_to_save = os.path.join("analysis","election_analysis.txt")
#1.initialize a total vote ocunter
total_votes = 0
#candidate options and canidate votes
candidate_options = []
#declare the empty dictionary canidate votes
candidate_votes = {}
#winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0 
#
#Open the election results and read the file
with open(file_to_load) as election_data:
    #read the file object with the reader function. 
    file_reader=csv.reader(election_data)
    #read header row
    headers= next(file_reader)
    #
    #print each row in the csv file
    for row in file_reader:
        #2. Add to the total vote count
        total_votes += 1
        #get the candidate name from each row.
        candidate_name = row[2] 
        #if candidate does not match any existing candidatek, add it to candidate list
        if candidate_name not in candidate_options:
        # add the candidate name to the candidate list
            candidate_options.append(candidate_name)
            #begin tracking that candidates vote count
            candidate_votes[candidate_name] = 0
        #add a vote to that ccanidates count
        candidate_votes[candidate_name] +=1
        #save the results to our text file
with open(file_to_save,"w") as txt_file:
            #print final vote cout to the terminal  
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
                #save the final vote count to the text file
    txt_file.write(election_results)
        #determine the percentage of votes for each candidate by looping throuhg the counts
        #1 iterate through the candidate list
    for candidate_name in candidate_votes:
        #2 Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
            #3 calculate the percentage of votes
        vote_percentage = round((float(votes)/ float(total_votes)*100),2) 
            #to do:print ou each candidates name, vote count, and percentage
            #of votes to the terminal
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)
            #Determine winning vote count and candidate
            #Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
                #if true then set winning_count= votes and winning_percent= vote percentage
            winning_count = votes
            winning_candidate = candidate_name 
            winning_percentage = vote_percentage       
        #print out the winning ccandidate, vote count and percentage to terminal
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    #save winning candidates results to the text file
    txt_file.write(winning_candidate_summary)
