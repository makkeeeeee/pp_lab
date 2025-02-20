import datetime

#Task 1 current day and 5 days ago 
current_date = datetime.date.today()
new_date = current_date - datetime.timedelta(days = 5)
print(f"The current data is {current_date}")
print(f"The date 5 days ago was {new_date}")


#Task 2 yesterday ,today ,tommorow
today = datetime.date.today()
yesterday= today - datetime.timedelta(days=1)
tommorow = today + datetime.timedelta(days =1)
print(f"yesterday is {yesterday}")
print(f"today is {today}")
print(f"tommorow is {tommorow}")

#Task 3 Drop microseconds from a datetime
date = datetime.datetime.now()
new_date = date.replace(microsecond = 0)

print(f"date time without microseconds is ",{new_date})

#Task 4 difference in seconds
date1 = datetime.datetime(2025,2,18,12,0,0)
date2 = datetime.datetime(2025,2,19,12,0,0)
diff = (date2 - date1).total_seconds()
print(f"diffrent between two date is {diff}")





