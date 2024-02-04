from modules.divider import divider
import datetime


now = datetime.datetime.now()
print(now)


divider()


date = datetime.date(2020, 1, 1)
print(date)


divider()


time = datetime.time(12, 30, 45)
print(time)


divider()


year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute
second = now.second

print(f"{year}/{month}/{day} {hour}:{minute}:{second}")
