# the data we need to retrieve.
# 1. the total number of votes cast
# 2. a complete list of candidates who received votes
# 3. the percentage of votes each candidate won
# 4. the total number of votes each candidate won
# 5. the winner of the election based on popular vote

# ======================================================================================
#                            DIRECT PATH TO READ
# # direct path to csv file
# # Assign a variable for the file to load and the DIRECT path
# file_to_load = 'Resources/election_results.csv'

# # Open the election results and read the file using the Open and Close function
# # create election_data as file variable
# election_data = open(file_to_load, 'r')

# # To do: perform analysis

# # close the file
# election_data.close

# #  OR OR OR Open the election results and read the file using the WITH option so don't
# # need to worry about closing the Open
# with open(file_to_load, 'r') as election_data:

#     # to do: perform analysis
#     print(election_data)

# ================================================================================================
#                               INDIRECT PATH to READ
# # import modules
# import csv
# import os

# # Assign a variable for the file to load and the path using the os module and INDIRECT path
# file_to_load = os.path.join("Resources", "election_results.csv")

# # open the election results and read the file
# with open(file_to_load, 'r') as election_data:

#     # print the file object
#     print(election_data)

# =================================================================================================
# #                   INDIRECT PATH  to WRITE
# import csv
# import os

# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# # using the open() function with the "w" mode we will write data to the file
# open(file_to_save, "w")

# =============================================================================================
#                   WRITE SOMETHING TO TXT FILE

# import csv
# import os

# # Create a filename variable to a direct or indirect path to the file.
# # analysis is folder name     
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# # open the file as a text file
# outfile = open(file_to_save, 'w')

# # Write some data to the file
# outfile.write("hello world")

# # close the file
# outfile.close()

# ======================================================================================
#                       WRITE SOMETHING TO TEXT FILE USING WITH statement
# import csv
# import os

# # Create a filename variable to a direct or indirect path to the file.
# # analysis is folder name     
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# # using the with statement open the file as a text file
# with open(file_to_save, "w") as txt_file:

#     # write data fo the file in one row
#     #txt_file.write("Arapahoe, Denver, Jefferson")

#     # write data to file in 3 rows
#     txt_file.write("Counties in the Election\n-----------\nArapahoe\nDenver\nJefferson")

# ============================================================================================
#                       3.4.4 READ the ELECTION RESULTS
# add our dependencies
import csv
import os

# assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")

# assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# initial total votes to zero before open the csv file so always start at zero
total_votes = 0

# list of candidates from 3rd column of data
candidate_options = []

# dictionary of candidate votes
candidate_votes = {}

# winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# open the election results and read the file
with open(file_to_load) as election_data:

    # to do: read and analyze the data here
    # read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Read the header row
    headers = next(file_reader)

    # print each row in the CSV rile
    for row in file_reader:
        # add to the total vote count increment by 1
        total_votes += 1

        # Ge the candidate name from each row with 3rd column
        candidate_name = row[2]

        # add the candidate name to the candidate list - will get everything in column
        # candidate_options.append(candidate_name)

        # if the candidate does not match any existing candidate (to get unique names)
        if candidate_name not in candidate_options:
            # add it to the list of candidates
            candidate_options.append(candidate_name)

            # begin tracking candidate's vote count in dictionary
            candidate_votes[candidate_name] = 0

    # add a vote to that candidate's count to get their total
        candidate_votes[candidate_name] += 1

# save the results to our text file
with open(file_to_save, "w") as txt_file:

     # after opening the file,Print the final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"total votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
        
     # after printing final vote count to terminal, Save the final vote count to the text file
    txt_file.write(election_results)

    # determine the percentage of votes for each candidate by looping through the counts
    # iterate through the candidate list
    for candidate_name in candidate_votes:
        # retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        # calculate the percentage of votes and change to float from int
        vote_percentage = float(votes) / float(total_votes) * 100
        # print the candidate name and percentage of votes to 1 decimal place
        #print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        
        # of the votes to the terminal.
        #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        
        # print final candidate results to the terminal
        print(candidate_results)

        #save the andidate results to our text file
        txt_file.write(candidate_results)
        # determine winning vote count and candidate
        # determine if the votes is greater than the winning coount
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # if true then set winning_count = votes and winning_percent = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # and set the winning candidate equal to the candidate's name
            winning_candidate = candidate_name

    # print the winning candidate's results to terminal
    winning_candidate_summary = (
        f"--------------------\n"
        f"winner: {winning_candidate}\n"
        f"winning vote count: {winning_count:,}\n"
        f"winning percentage: {winning_percentage:.1f}%\n"
        f"---------------------\n")

    print(winning_candidate_summary)


    #save the winning candidate's results to the text file
    txt_file.write(winning_candidate_summary)
   

    # to do:  print out the winning candidate, vote count and percentage to terminal




# print the candidate dictionary
#print(candidate_votes)

# print the candidate ist
#print(candidate_options)
    
# print the total votes outside the for  loop
#print(total_votes)
    
    ## Read and print the header row.
    #   headers = next(file_reader)
    #       print(headers)

    # # print each row in the csv file
    # for row in file_reader:
    #     print(row)




