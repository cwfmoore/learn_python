import datetime as dt

date = dt.datetime(year=1956, month=1, day=31)

# print(f'Guido van Rossum was born {date:%d, %b %Y}')

print(f'Guido van Rossum was born {date:%Y-%m-%d}')

