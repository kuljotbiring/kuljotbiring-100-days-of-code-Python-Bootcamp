import datetime as dt

now = dt.datetime.now()
# you can get specific pieces of the datetime object as shown below
year = now.year
month = now.month
# gives a number with 0 being Monday 1 being Tuesday etc...
day_of_week = now.weekday()
print(now)

# can specify a date time object from scratch
date_of_birth = dt.datetime(year=1995, month=12, day=15)
print(date_of_birth)
