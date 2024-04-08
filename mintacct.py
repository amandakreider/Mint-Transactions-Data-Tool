import json
import pandas as pd
from pathlib import Path
import os

# Initiate lists and dictionaries
paths = []
mykeys = []
accountids = []
ids = []
altids = []
accountnums = []
types = []
descs = []
dates = []
normals = []
nicknames = []
providers = []
Dup = {}

# Define list of relevant paths
directory = str(Path(__file__).parent) + '/'
    
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith('txt') and filename.startswith('accounts_users'):
        paths.append(os.path.join(directory, filename))
        continue
    else:
        continue

# Loop over paths 
for thispath in paths:

	myfile = open(thispath).read()
	data = json.loads(myfile)

	for num in range(len(data)):

		mylist = list(data[num].keys())

		for i in range(len(mylist)):

			if mylist[i] in Dup:
			    ItemNumber = Dup[mylist[i]]
			else:
			    mykeys.append(mylist[i])
			    Dup[mylist[i]] = ItemNumber = len(mykeys)-1		

print(mykeys)

# Loop over transactions files to save values from relevant keys 
for thispath in paths:

	myfile = open(thispath).read()
	data = json.loads(myfile)

	print(data[7])

	# Loop over transactions
	for i in data: 

		if 'accountId' in i:
			accountids.append(i['accountId'])
		else:
			accountids.append('')

		if 'id' in i:
			ids.append(i['id'])
		else:
			ids.append('')

		if 'alternateIds' in i:
			altids.append(i['alternateIds'])
		else:
			altids.append('')

		if 'nickName' in i:
			nicknames.append(i['nickName'])
		else:
			nicknames.append('')

		if 'accountNumberMasked' in i:
			accountnums.append(i['accountNumberMasked'])
		else:
			accountnums.append('')

		if 'accountType' in i:
			types.append(i['accountType'])
		else:
			types.append('')

		if 'description' in i:
			descs.append(i['description'])
		else:
			descs.append('')

		if 'createdTimestamp' in i:
			dates.append(i['createdTimestamp'])
		else:
			dates.append('')

		if 'normalizedAccountType' in i:
			normals.append(i['normalizedAccountType'])
		else:
			normals.append('')

		if 'providerName' in i:
			providers.append(i['providerName'])
		else:
			providers.append('')
	
# Create a csv file with transaction data
df = pd.DataFrame()

df['Account ID'] = accountids
df['Alternate IDs'] = altids
df['ID'] = ids
df['Nickname'] = nicknames
df['Provider Name'] = providers
df['Created on'] = dates
df['Account Number'] = accountnums
df['Type'] = types
df['Normalized Type'] = normals
df['Description'] = descs

print("csv file will be generated at ", directory)
df.to_csv(directory+'accounts.csv')




	