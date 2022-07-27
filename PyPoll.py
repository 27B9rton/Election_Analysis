#Steps to Analyze Election

#1. Find the total number of votes cast in the election
#2. Create a list of all candidates receiving votes
#3. Find out how many votes each candidate got and turn that into a percentage of the total vote
#4. Declare a winner based off the popular vote

import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

#Create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")

# #Use the open statement to open the file as a text file and create data.
# with open(file_to_save, "w") as txt_file:
#   txt_file.write("\nArapahoe\nDenver\nJefferson")  

#Set Voter Counter to 0
total_votes = 0

candidate_options = []

#Create dictionary for votes per Candidate
candidate_votes = {}


# Find the winning candidate and Winning Count
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# # Open the election results and read the file. 
# with open(file_to_load) as election_data:

#     # Print the file object.
#      print(election_data)


# To do read and analyze data
with open(file_to_load) as election_data:
  file_reader = csv.reader(election_data)

  # Read & Print header row in the CSV file
  headers = next(file_reader)


  #Print each row in the CSV file
  for row in file_reader:

    #add to the total vote count.
    total_votes +=1

    #Print Candidate Name from each row
    candidate_name = row[2]

    # Add candidate name to candidate options
    if candidate_name not in candidate_options:
       
        candidate_options.append(candidate_name)
       
       #Track Candidates vote count
        candidate_votes[candidate_name] = 0
    
    candidate_votes[candidate_name]+= 1

#Save results to text file    
with open(file_to_save, "w") as txt_file:

  election_results =(
          f"\nElection Results\n"
          f"-------------------------\n"
          f"Total Votes: {total_votes:,}\n"
          f"-------------------------\n")
  print(election_results, end="")
      # Save the final vote count to the text file.
  txt_file.write(election_results)
  
  for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        votepercentage = float(votes) / float(total_votes) * 100
        #print(f"{candidate_name}: {votepercentage:.1f}% ({votes:,})\n")
        candidate_results = (f"{candidate_name}: {votepercentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)

        if (votes > winning_count) and (votepercentage > winning_percentage):
    # 2. If true then set winning_count = votes and winning_percent =
    # vote_percentage.
            winning_count = votes
            winning_percentage = votepercentage
    # 3. Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name

  #winning candidate summary
  winning_candidate_summary = (
    f"---------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winner Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"----------------------------\n")

  #print(winning_candidate_summary)
  