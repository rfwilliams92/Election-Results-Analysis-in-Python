# Election-Results-Analysis-in-Python
## Overview of Election Audit 
Write a python script that will be able to read a csv file with voter data and deliver election results, county-by-county turnout, and the winner of the election based on popular vote.

### Purpose
A concise python script with the ability to deliver the following information for an election audit: total number of votes cast, a complete list of candidates who received votes, total number of votes each candidate received, the percentage of votes each candidate won, the winner of the election based on popular vote, voter turnout for each county, percentage from each county out of total turnout, and county with highest turnout.


## Election-Audit Results
### How many votes were cast in this congressional election? 
- 369,711. Since each row was a vote cast the code block was simple. Set total_votes to 0 and add a for loop:
```
total_votes = 0
For row in csvreader:
	total_votes += 1
```

### Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
- This code block calls a for loop on county_name in the counties list:
```
for county_name in counties:
    county_vote_count = votes_by_county[county_name]

    percentage_votes_county[county_name] = float(county_vote_count) / float(total_votes) * 100
   
   county_results = f"{county_name}:{county_vote_count/ total_votes * 100:.1f}% ({county_vote_count:,})”
```

### Which county had the largest number of votes?
- Denver. This code block sat within the for loop described in the county breakdown. It contains a conditional statement and a variable that is initiated as an empty string.
```
largest_county_turnout = “”
if county_vote_count > largest_county_count:
	largest_county_count = county_vote_count
	largest_county_turnout = county_name 
```
### Provide a breakdown of the number of votes and the percentage of the total votes each candidate received?
- This code block was similar in structure to how we got the breakdown of total for each county, just using a different variables.

Charles Casper Stockham:  23.0% (85,213)

Diana DeGette:  73.8% (272,892)

Raymon Anthony Doane:  3.1% (11,606)

### Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
- Again a similar structure to how we found the largest county turnout. A if conditional statement that compares votes of each candidate.

Winner: Diana DeGette

Winning Vote Count: 272,892

Winning Percentage: 73.8%


## Election-Audit Summary

This script can be flexible and utilized in other elections with some small modifications:
- A different csv file with voter data with similar objectives in analysis can be substituted into this python script.
- The script could be modified to account for political party demographics of voters, counties, and candidates with a few well placed AND conditionals in the existing code blocks, if data was provided.
