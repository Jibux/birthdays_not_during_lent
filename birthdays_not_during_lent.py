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

# Earliest easter day: 22/03
# Latest easter day: 25/04
# Earliest ash wednesday: 04/02
# Latest ash wednesday: 10/03
latest_easter_day = date(leap_year,4,25)
earliest_easter_day = date(leap_year,3,22)
latest_ash_wednesday = latest_easter_day - delta
earliest_ash_wednesday = earliest_easter_day - delta_leap

print("Earliest easter day:",earliest_easter_day.day,earliest_easter_day.month)
print("Latest easter day:",latest_easter_day.day,latest_easter_day.month)
print("Earliest ash wednesday:",earliest_ash_wednesday.day,earliest_ash_wednesday.month)
print("Latest ash wednesday:",latest_ash_wednesday.day,latest_ash_wednesday.month)

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









#def divmod2(x, y):
#    q, r = divmod(x, y)
#    if y<0:
#        return q+1, r+abs(y)
#    return q, r
#
## cycle de Méton
#(tmp,n) = divmod2(year,19)
## centaine et rang de l'année
#(c,u) = divmod2(year,100)
## siècle bissextile 
#(s,t) = divmod2(c,4)
## cycle de proemptose
#(p,tmp) = divmod2(c+8,25)
## proemptose
#(q,tmp) = divmod2(c-p+1,3)
## épacte
#(tmp,e) = divmod2(19*n+c-s-q+15,30)
## année bissextile
#(b,d) = divmod2(u,4)
## lettre dominicale 
#(tmp,L) = divmod2(2*t+2*b-e-d+32,7)
## correction
#(h,tmp) = divmod2(n+11*e+22*L,451)
## résultat
#(m,j) = divmod2(e+L-7*h+114,31)
#
#print(j+1,m)


