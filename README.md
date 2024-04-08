# Mint Transaction Data Conversion Tool
 
This project contains Python programs to convert exported transactions and accounts data from Mint.com (Intuit) to usable .csv files.

It is meant to help users convert their Mint data to a usable format now that the Mint app has been shut down.

To use the programs:

1. Navigate to the location on your computer where you've saved your Mint data download.

2. Save the programs mint.py and mintacct.py in the following folder within your Mint data download: ../SharedData/FinancialData.

3. Install the Python dependencies from requirements.txt.

4. Run the programs.
    - mint.py saves your Mint transactions data to a csv file
    - mintacct.py saves your Mint account data (i.e., a list of your accounts with associated account IDs) to a csv file
