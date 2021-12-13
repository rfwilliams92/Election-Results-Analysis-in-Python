#The data we need to retieve from CSV file
import pathlib
import csv 

csv_path= pathlib.Path('Resources/election_results.csv')

total_votes = 0

counties = []
votes_by_county = {}
percentage_votes_county = {}

largest_county_count = 0
largest_county_turnout = ""

canidate_options = []
canidate_votes = {}
percentage_votes = {}

winning_canidate = ""
winning_count = 0
winning_percentage = 0

with open("output/election_results.txt", "w") as textfile:

    with open(csv_path) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')

    #The total number of votes cast
        csv_header = next (csvreader)

        for row in csvreader:
            total_votes += 1
            
    #The complete list of candidates who recieved votes
            county_name = row[1]
            canidate_name = row[2]
           
            if canidate_name not in canidate_options:
                canidate_options.append(canidate_name)
                
                canidate_votes[canidate_name] = 0

            if county_name not in counties:
                counties.append(county_name)

                votes_by_county[county_name] = 0
           
            #The total number of votes each candidate won 
            canidate_votes[canidate_name] += 1
            votes_by_county[county_name] += 1
        
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n\n"
            f"County Votes:\n"
        )
        print(election_results, end="")
        textfile.write(election_results)

        for county_name in counties:
        # 6b: Retrieve the county vote count.
            county_vote_count = votes_by_county[county_name]
        # 6c: Calculate the percentage of votes for the county.
            percentage_votes_county[county_name] = float(county_vote_count) / float(total_votes) * 100
            county_results = f"{county_name}: {county_vote_count/ total_votes * 100:.1f}% ({county_vote_count:,})"
            
            print(county_results)
            textfile.write(f"{county_results}\n")

            if county_vote_count > largest_county_count:
                largest_county_count = county_vote_count
                largest_county_turnout = county_name
            
        county_summary = (
            f"\n-------------------------\n"
            f"Largest County Turnout: {largest_county_turnout}\n"
            f"-------------------------\n")
        
        print(county_summary)
        textfile.write(county_summary)
    
    #The percentage of votes each candidate won 
        for canidate_name in canidate_votes:
            votes = canidate_votes[canidate_name]
            votes_percentage = float(votes) / float(total_votes) * 100
            
            print(f"{canidate_name}: {votes_percentage: .1f}% ({votes:,})\n")
            textfile.write(f"{canidate_name}: {votes_percentage: .1f}% ({votes:,})\n")

            #The winner of the election by popular vote   
            if (votes > winning_count) and (votes_percentage > winning_percentage):
                winning_count = votes
                winning_percentage = votes_percentage
                winning_canidate = canidate_name
        
            winning_canidate_summary = (
                f"--------------------------\n"
                f"Winner: {winning_canidate}\n"
                f"Winning Vote Count: {winning_count:,}\n"
                f"Winning Percentage: {winning_percentage:.1f}%\n"
                f"--------------------------\n"
            )
        print (winning_canidate_summary)
        textfile.write(winning_canidate_summary)
