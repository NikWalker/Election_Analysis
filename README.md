# Election Analysis
## Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.
1. The total number of votes cast.
2. A complete list of candidates who received votes.
3. The percentage of votes each candidate won.
4. The total number of votes each candidate won.
5. The winner of the election based on popular vote.

Furthermore, for this challenge, the Board of Elections has requested the following additional information.

6. The voter turnout for each county
7. The percentage of votes for each county from the total vote count.
8. The county with the highest turn out. 

## Resources
- Data source: election_results.csv
- Software: Python 3.6.1, Visual Studio Code, 1.38.1

## Election Audit Results
The analysis of the election show that:

- There were 369,711 votes cast in the election.
- The candidates were:
  - Charles Casper Stockham:
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate results were:
  - Charles Casper Stockham received 85,213 votes, which was 23.1% of the votes.
  - Diana DeGette received 272,892 votes, which was 73.8% of the votes.
  - Raymon Anthony Doane received 11,606 votes, which was 3.1% of the votes.
- The winner of the election was: 
  - Diana DeGette received 272,892 votes, which was 73.8% of the votes.
- The votes for each county were:
  - Jefferson County had 38,855 votes which accounted for 10.5% of the state’s votes.
  - Denver County had 306,055 votes which accounted for 82.8% of the state’s votes.
  - Arapahoe County had 24,801 votes which accounted for 6.7% of the state’s votes.
- The county with the highest voter turnout:
  - Denver County with 82.8% of Colorado's total vote count.

## Election Audit Summary

In the Colorado election, there were three candidates who received votes: Charles Casper Stockham, Diana DeGette and Raymon Anthony Doane. The winner of the election, Diana DeGette, won with a majority of 73.8% of the 369,711 total votes cast.  The votes cast came from Denver, Jefferson, and Arapahoe counties. In this analysis, the use of decision and repetition statements, such as "for loops" and "if statements" were conducted to create [code](PyPoll_challenge.py) that explored voter turnout for each county. This code could be used in later elections. A new csv could be read into the code, if the csv is in the same format [Ballot ID, County, Candidate].  After creating the code, an [election analysis](Analysis/election_analysis.txt) output document was printed to present to the Colorado Board of Elections representing the results of the election, as well as county analytics. Denver county had the largest voter turnout, with 306,055 votes. This accounts for 82.8% of the state’s total votes, where the next largest voter turnout came from Jefferson county with only 10.5% of the state’s votes. 
