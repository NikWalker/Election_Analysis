counties_dict={}
counties_dict['Arapahoe']=422829
counties_dict['Denver']=463353
counties_dict['Jefferson']=432438
voting_data=[]
voting_data.append({'county':'Arapahoe','registered_voters':422829}) 
voting_data.append({'county':'Denver','registered_voters':463353}) 
voting_data.append({'county':'Jefferson','registered_voters':432438}) 
for county_dict in voting_data:
    print(county_dict)
for i in range

counties_dict={'Arapahoe':422829,'Denver':463353,'Jefferson':432438}
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")


    #The data we need to retrieve.
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote