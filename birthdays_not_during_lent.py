#!/usr/bin/python3


import calendar
import sys

from dateutil.relativedelta import *
from dateutil.easter import *
from datetime import *

number_of_years_to_check = 100

def usage():
    print('Usage:',sys.argv[0],'day_of_birth number_of_years_to_check')
    print('day_of_birth format: yyyy-mm-dd')

if len(sys.argv) < 2:
    usage()
    sys.exit(1)
else:
    input_day_of_birth = sys.argv[1]

if len(sys.argv) == 3:
    number_of_years_to_check = abs(int(sys.argv[2]))

try:
    (year_of_birth, month_of_birth, day_of_birth) = [ abs(int(n)) for n in input_day_of_birth.split('-') ]
    person_date_of_birth = date(year_of_birth,month_of_birth,day_of_birth)
except:
    print("Input error: day_of_birth is not correctly formated or does not exist!\n")
    usage()
    sys.exit(1)

delta = relativedelta(days=46)
delta_leap = relativedelta(days=47)

leap_year = 1904
person_date_of_birth_on_leap_year = date(leap_year,month_of_birth,day_of_birth)

# Earliest Easter day: 22/03
# Latest Easter day: 25/04
# Earliest Ash Wednesday: 04/02
# Latest Ash Wednesday: 10/03
latest_easter_day = date(leap_year,4,25)
earliest_easter_day = date(leap_year,3,22)
latest_ash_wednesday = latest_easter_day - delta
earliest_ash_wednesday = earliest_easter_day - delta_leap

if person_date_of_birth_on_leap_year >= latest_easter_day or person_date_of_birth_on_leap_year < earliest_ash_wednesday:
    print("You will never have your birthday during Lent.")
    sys.exit(0)

if person_date_of_birth_on_leap_year < earliest_easter_day and person_date_of_birth_on_leap_year >= latest_ash_wednesday:
    print("You will always have your birthday during Lent.")
    sys.exit(0)



for year in range(year_of_birth, year_of_birth + number_of_years_to_check):
    easter_day = easter(year,3)
    ash_wednesday = easter_day - delta

    if month_of_birth == 2 and day_of_birth == 29 and not calendar.isleap(year):
        person_birthday = date(year,3,1)
    else:
        person_birthday = date(year,month_of_birth,day_of_birth)

    if ash_wednesday > person_birthday or easter_day <= person_birthday:
        print(year)


