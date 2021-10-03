############################################################
# Python Age App
# Created by: Joel Anderton
# Date: 10/10/2017
# Updated: 2/10/2021
# Calculates a person's age to 1 decimal place
#
# Updates: 2/10/2021 - added a new "mode": given the age, find
#                    the possible date range for DOB
#
############################################################
from datetime import date, datetime, timedelta
import math 

# Birth Date
#bday = date(2012, 12, 7)

quit = 'n'
while quit != 'y':
    print('Mode 1 - Find Age (enter "1")')
    print('Mode 2 - Find Date Range of DOB given Age (enter "2")')
    mode = input('Which mode would you like: ')

    if mode == '1':
        date_entry = input('Enter a date of birth MM/DD/YYYY format: ')
        month, day, year = map(int, date_entry.split('/'))
        bday = date(year, month, day)

        # Date
        #date2 = date(2016, 11,23)
        date_entry = input('Enter a date in MM/DD/YYYY format: ')
        month, day, year = map(int, date_entry.split('/'))
        date2 = date(year, month, day)


        # Subtract dates to get number of days
        days = (date2 - bday).days

        # Convert days to years
        years = math.floor((days / 365.25)*10)/10

        # Print out number of years
        print(years)
    
    elif mode == '2':
        age = float(input('Age: '))
        date_entry = input('Enter a date in MM/DD/YYYY format: ')
        month, day, year = map(int, date_entry.split('/'))
        date2 = date(year, month, day)

        # Get days
        days = (age * 365.25)
        #print(days)

        dob1 = date2 - timedelta(days=days) # find date given days
        print('Date of Birth is sometime between:')
        print(dob1 - timedelta(days=37)) # find first date given days
        print(dob1 - timedelta(days=1)) # find last date given days
        

    else:
        print('Please enter either a 1 or 2')
    quit = input('Do you want to quit? y/n: ')
