
############################################################
# Python Age App
# Created by: Joel Anderton
# Date: 10/10/2017
# Updated: 11/14/2017
# Calculates a person's age to 1 decimal place
############################################################
from datetime import date, datetime
import math 

# Birth Date
#bday = date(2012, 12, 7)
quit = 'n'
while quit == 'n':
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
    
    quit = input('Do you want to quit? y/n: ')
