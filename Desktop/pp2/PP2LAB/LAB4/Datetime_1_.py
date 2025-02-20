#Datetime
"" """
datetime 模块是 Python 标准库中用于处理日期和时间的强大工具，下面为你介绍其中一些常用的类和方法：
常用类

datetime.date：用于表示日期，包含年、月、日。
datetime.time：用于表示时间，包含时、分、秒、微秒和时区信息。
datetime.datetime：是 date 和 time 的结合，包含日期和时间的所有信息。
datetime.timedelta：表示两个日期或时间之间的差值。
常用方法
1. datetime.datetime.now()
返回当前的日期和时间。

2. datetime.datetime.strptime(date_string, format)
将字符串解析为 datetime 对象，需要指定字符串的格式。

"""

import datetime

now = datetime.datetime.now()
print(now)
print(now.year)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

my_date = datetime.datetime(2023,9,21,22,35,0)
print(my_date)

formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_date)

