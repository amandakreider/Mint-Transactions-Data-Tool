import json
import pandas as pd
from pathlib import Path
import os

# Initiate lists and dictionaries
amounts = []
cats = []
descriptions = []
merchants = []
transdates = []
postdates = []
modified = []
alts = []
altscat = []
ids = []
methods0 = []
methods1 = []
methods2 = []
methods3 = []
methods4 = []
methods5 = []
methods = [methods0, methods1, methods2, methods3, methods4, methods5]
cards = []
paths = []
mykeys = []
Dup = {}

# Define list of relevant transactions files
directory = str(Path(__file__).parent) + '/'
    
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith('txt') and filename.startswith('transactions_users'):
        paths.append(os.path.join(directory, filename))
        continue
    else:
        continue

# Loop over transactions files to print a list of possible keys
for thispath in paths:

	myfile = open(thispath, encoding="UTF-8").read()
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

	myfile = open(thispath, encoding="UTF-8").read()
	data = json.loads(myfile)

	# Loop over transactions
	for i in data: 

		if 'transactionDate' in i:
			transdates.append(i['transactionDate'])
		else:
			transdates.append('')

		if 'postedDate' in i:
			postdates.append(i['postedDate'])
		else:
			postdates.append('')

		if 'amount' in i:
			amounts.append(i['amount'])
		else:
			amounts.append('')

		if 'categoryName' in i:
			cats.append(i['categoryName'])
		else:
			cats.append('')

		if 'merchantCategoryName' in i:
			altscat.append(i['merchantCategoryName'])
		else:
			altscat.append('')

		if 'description' in i:
			descriptions.append(i['description'])
		else:
			descriptions.append('')

		if 'merchant' in i:
			merchants.append(i['merchant'])
		else:
			merchants.append('')

		if 'lastModifiedTimestamp' in i:
			modified.append(i['lastModifiedTimestamp'])
		else:
			modified.append('')

		if 'L10_provider_description' in i:
			alts.append(i['L10_provider_description'])
		else:
			alts.append('')

		if 'transactionId' in i:
			ids.append(i['transactionId'])
		else:
			ids.append('')

		for methnum in range(2):
			if 'associations' in i:
				methods[methnum].append(i['associations'][methnum])
			else:
				methods[methnum].append('')		

		if 'cardNumber' in i:
			cards.append(i['cardNumber'])
		else:
			cards.append('')
	
# Create a csv file with transaction data
df = pd.DataFrame()

df['Posted'] = postdates
df['Transaction Date'] = transdates
df['Category'] = cats
df['Merchant Category'] = altscat
df['Amount'] = amounts
df['Description'] = descriptions
df['Alternate Description'] = alts
df['Method 1'] = methods0
df['Method 2'] = methods1
df['Card'] = cards
df['Merchant'] = merchants
df['Transaction ID'] = ids
df['Last Modififed'] = modified

print("csv file will be generated at ", directory)
df.to_csv(directory+'transactions.csv')


