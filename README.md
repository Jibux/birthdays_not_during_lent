# Birthdays not during Lent

## Description
This simple script output the years when a birthay is not during Lent.

## Usage
```
./birthdays_not_during_lent.py day_of_birth number_of_years_to_check
day_of_birth format: yyyy-mm-dd
number_of_years_to_check: number (default is 100)
```

## Info
* Earliest Easter day: 22nd of March
* Latest Easter day: 25th of April
* Earliest Ash Wednesday: 4th of February
* Latest Ash Wednesday: 10th of March

## Examples
```
./birthdays_not_during_lent.py 2018-3-5 20
2019
2030
```
```
./birthdays_not_during_lent.py 2018-1-1
You will never have your birthday during Lent.
```
```
./birthdays_not_during_lent.py 2018-3-11
You will always have your birthday during Lent.
```

