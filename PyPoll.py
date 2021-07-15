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

# open the election results and read the file
with open(file_to_load) as election_data:

    # to do: read and analyze the data here
    # read the file object with the reader function
    file_reader = csv.reader(election_data)

    # print the header row for example
    headers = next(file_reader)
    print(headers)

    # # print each row in the csv file
    # for row in file_reader:
    #     print(row)




