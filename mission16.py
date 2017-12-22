import calendar

def func1(x):
    if x%400 == 0 or (x % 4 == 0 and x%100 != 0):
        return x
    else:
        return 0

leap_year = list(filter(func1, range(1006, 1996, 10)))
leap_year2 = list(filter(lambda x:x%400 == 0 or (x % 4 == 0 and x%100 != 0),range(106, 1996)))
print(leap_year)

year = [year for year in leap_year if calendar.weekday(year, 1, 1) == 3] #datetime.date(year, 1, 26).isoweekday() == 1
print(year)

#method1:
print('method1:')
import calendar
import datetime
leap_year = [year for year in range(1006, 1996,10) if calendar.isleap(year)]
result_year = [year for year in leap_year if datetime.date(year, 1, 1).isoweekday() == 4]
print(result_year)
