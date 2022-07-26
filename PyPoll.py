#Steps to Analyze Election

#1. Find the total number of votes cast in the election
#2. Create a list of all candidates receiving votes
#3. Find out how many votes each candidate got and turn that into a percentage of the total vote
#4. Declare a winner based off the popular vote

import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Print the file object.
     print(election_data)

#Create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Use the open statement to open the file as a text file.
with open(file_to_save, "w") as txt_file:

#Create data in file
  txt_file.write("Arapahoe, ")
  txt_file.write("Denver, ")
  txt_file.write("Jefferson")

