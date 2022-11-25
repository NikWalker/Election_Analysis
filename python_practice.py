counties=["Arapahoe","Denver","Jefferson"]
if counties[1]=='Denver':
    print(counties[1])
if 'El Paso' in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not in the list of counties.")
if 'Arapahoe' in  counties and 'El Paso'not in counties:
    print("only Arapahoe and El Paso are in the list of counties")
else:
    print('Arapahoe or El Paso is not in the list of counties') 
for county in counties:
    print(county)      
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}   
for county in counties_dict.keys():
    print (county)
for voters in counties_dict.values():
    print (voters)
for county, voters in counties_dict.items():
    print(county,'county has', voters,'registered voters.')