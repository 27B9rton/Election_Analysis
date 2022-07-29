# Election_Analysis
Election Analysis using software Python 3.9.5. and Visual Studio Code

## Project Overview

Colorado Board of Elections has asked us to review and audit the recent local election to find the winner as well as voter turnout by county.

## Summary
The election analysis shows that:
- There were 369,711 total votes cast.
- Denver had the highest voter turnout with 306,055 votes. That is 82.78% of the total vote.
- Jefferson County was next with 38,855 votes cast. Tha'ts 10.51% of the total vote.
- Arapahoe County had 24,801 votes cast. This is 6.71% of the total vote.


- There were 3 total candidates
  - Charles Casper Stockham who received 85,213 votes (23%)
  - Diana DeGette who received 272,892 votes (73.8%)
  - Raymon Anthony Doane who received 11,606 votes (3.1%)


The winner of the election was
 Diana DeGette, who received 73.8% of the vote and 272,892 total votes.
 
The committee can continue to use some of this script in future election audits.
The following script may be refactored into future elections to find Candidate names, candidate votes, county names, and county votes.

    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county = row[1]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county not in county_list:

            # 4b: Add the existing county to the list of counties.
            county_list.append(county)

            # 4c: Begin tracking the county's vote count.
            county_vote[county] = 0

        # 5: Add a vote to that county's vote count.
        county_vote[county] +=1
 
 ##Challenge Overview
 I enjoyed this challenging exercise. Once again, working with arrays and dictionaries proved to be most difficult for me, but I managed to keep them organized and properly integrated.

