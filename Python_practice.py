"""
counties = ["Arapahoe", "Denver", "Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])
"""
#Using IN operator
'''
counties = ["Arapahoe", "Denver", "Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties")
else:
    print("El Paso is not in the list of counties")
'''
#using AND operator
'''
counties = ["Arapahoe", "Denver", "Jefferson"]
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties")
else:
    print("Arapahoe or El Paso is not in the list of counties")
'''

#using OR operator
'''
counties = ["Arapahoe", "Denver", "Jefferson"]
if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso are in the list of counties")
else:
    print("Arapahoe and El Paso are not in the list of counties")

# county variable is declared below - looking in counties and returns
# each item listed until there are no more
for county in counties:
    print(county)
'''

# Range example part 1
'''
numbers = [0, 1, 2, 3, 4, 5]
for num in numbers:
    print(num)
'''


# Range example part 2 written another way - same as above but 
'''
#using range() function
for num in range(5):
    print(num)
'''

#Iterate through a Dictionary
#counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

# Get keys of a dictionary method 1
'''
for county in counties_dict:
    print(county)
'''


# Get keys of a dictionary method 2
'''
for county in counties_dict.keys():
    print(county)
'''
# skill drill 3.2.10 w/ concat
'''
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, voters in counties_dict.items():
    print(county + "county has" + str(voters) + "registered voters.")
'''

# modified skill drill w/ F-Strings
'''
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")
'''



# list of dictionaries
'''
voting_data = [{"county": "Arapahoe", "registered_voters": 422829},
                {"county": "Denver", "registered_voters": 463353},
                {"county": "Jefferson", "registered_voters": 432438}]
'''

'''
for county_dict in voting_data:
    print(county_dict)
'''
# using range() and len()
'''
for county in range(len(voting_data)):
    print(voting_data[county]['county'])
'''
# nested for loop to get values() 
'''
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)
'''
# only print value for registered_voters
'''
for county_dict in voting_data:
    print(county_dict['registered_voters'])
'''
# only print value for county
'''
for county_dict in voting_data:
    print(county_dict['county'])
'''

# f string multiple outputs
# added :, after variable i f string to notate adding commas to value
# added :.2f to percentage value to notate adding 2 decimal places
'''
candidate_votes = int(input("how many votes did the candidate get in the election ?"))
total_votes = int(input("What is the total number of votes in the election?"))
message_to_candidate = (
    f"you received {candidate_votes:,} number of votes"
    f"the total number of votes in the election was {total_votes:,}"
    f"you received {candidate_votes/total_votes * 100:.2f} % of the total votes")

print(message_to_candidate)
'''

# Skill Drill 3.2.11  1
'''
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")
'''
# Skill Drill 3.2.11  2

voting_data = [{"county": "Arapahoe", "registered_voters": 422829},
                {"county": "Denver", "registered_voters": 463353},
                {"county": "Jefferson", "registered_voters": 432438}]
for county_dict in voting_data:
    print(f"{county_dict['county']} county has {county_dict['registered_voters']:,} registered voters." )