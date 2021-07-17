# Election-Analysis
Module 3

## Project Overview of Election Audit

A Colorado Board of Elections has acked for the following tasks to complete the electiion audit of a recent
local congressional election.

1. Calculate the total number of votes cast
2. Get a complete list of canddidate who received votes
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won
5. Determine the winner of the election based on popular vote

## Resources - Election Audit Results

- Data Source: election_results.csv
- Data Output: election_analysis.txt
- Software: Python 3.6.7, Visual Studio Code, 1.38.1

The following includes outcomes for the congressional election.  We were able to determine what candidate won
and show distribution of voting by each county.

We produced the outcome to the terminal.

![Terminal Outcome](https://github.com/ckbauman/Election-Analysis/blob/main/analysis/Terminal_Output.png)

We also produced the outcome to a txt file (located in the **Analysis** folder)

![Textfile Outcome](https://github.com/ckbauman/Election-Analysis/blob/main/analysis/Textfile_Output.png)

Our primary outcomes conclude:

- How many votes were cast in this congressional election?

![election total](https://github.com/ckbauman/Election-Analysis/blob/main/analysis/Election_total.png)

- Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.

![counties breakout](https://github.com/ckbauman/Election-Analysis/blob/main/analysis/Counties_breakout.png)

- Which county had the largest number of votes?

![counties winner](https://github.com/ckbauman/Election-Analysis/blob/main/analysis/counties_winner.png)

- Provide a breakdown of number of votes and percentage of total votes each candidate received.

![candidate breakout](https://github.com/ckbauman/Election-Analysis/blob/main/analysis/Candidate_breakout.png)

- Which candidate won the election, what was their perentage of the total votes?

![candidate winner](https://github.com/ckbauman/Election-Analysis/blob/main/analysis/Candidate_winner.png)

We were able to produce this information using python code below:

1. Initialize a county list that will hold the names of the counties.  Initialize a dictionary that will hold the county as the key and the votes cast for each county as the values.
> county_options = []
> 
> county_votes = {}

2. Initialize an empty string that will hold the county name for the county with the largest turnout. Initialize a variable that will hold the number of votes of the county that had the largest turnout.
>high_county = ""
>
> high_count = 0
> 
>high_percentage = 0

3. While reading the election results from each row inside the for loop, write a script that gets the county name from each row.
> county_name = row[1]
> 
4. Write a decision statement with a logical operator to check if the county name acquired in Step 3 is in the county list you created in Step 1. Write a script that initializes the county vote to zero, like you did when you began to track the vote counts for the candidates.  Write a script that adds a vote to the county’s vote count as you are looping through all the rows, like you did for the candidate’s vote count.
> 4a: Write an if statement that checks that the county does not match any existing county in the county list.
        if county_name not in county_options:

            # 4b: Add the existing county to the list of counties.
            county_options.append(county_name)

            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0
5.
- Write a repetition statement to get the county from the county dictionary that was created in Step 1.
- Initialize a variable to hold the county’s votes as they are retrieved from the county votes dictionary.
- Write a script that calculates the county’s votes as a percentage of the total votes.
- Write a print statement that prints the current county, its percentage of the total votes, and its total votes to the command line.
- Write a script that saves each county, the county’s total votes, and the county’s percentage of total votes to the election_results.txt file.
- Write a decision statement that determines the county with the largest vote count and then adds that county and its vote count to the variables created in Step 2.
8.  Write a print statement that prints out the county with the largest turnout.
9.  Write a script that saves the county with the largest turnout to the election_results.txt file.


## Summary

The analysis of the election show that:
- The candidates were:
  - candidate 1
  - candidate 2
  - canddidate 3
- The candidate results were:
  - candidate 1 recived x% of the vote and y number of votes
  - candidate 2 received x% of the vote and y number of votes
  - candidate 3 received x% of the vote and y number of votes
- The winner of the election was:
  - Candidate 1,2,3 who received x% of the vote and y number of votes

## Challenge Overview

## Challenge Summary
