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

#Use the open statement to open the file as a text file and create data.
with open(file_to_save, "w") as txt_file:
  txt_file.write("\nArapahoe\nDenver\nJefferson")  

#Set Voter Counter to 0
total_votes = 0

candidate_options = []

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Print the file object.
     print(election_data)


# To do read and analyze data
with open(file_to_load) as election_data:
  file_reader = csv.reader(election_data)

  # Read & Print header row in the CSV file
  headers = next(file_reader)


  #Print each row in the CSV file
  for row in file_reader:

    #add to the total vote count.
    total_votes +=1
    print(total_votes)