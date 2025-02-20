"""""
1. 字符串与 datetime 对象的相互转换
字符串转 datetime 对象
使用 strptime 方法:datetime.datetime.strptime(date_string, format) 是将字符串解析为 datetime 对象的关键方法。
date_string 是待解析的日期时间字符串，format 是该字符串对应的格式。例如代码中的 date_str = "12-02-2025 14:30"

2. timedelta 类的使用
创建 timedelta 对象:timedelta 类用于表示两个日期或时间之间的差值，也可用于日期和时间的加减运算。
通过 datetime.timedelta(days=5) 可以创建一个表示 5 天时间间隔的 timedelta 对象。
timedelta 还支持 weeks、hours、minutes、seconds、milliseconds、microseconds 等参数。
日期时间的加减运算：可以将 timedelta 对象与 datetime 对象进行加减操作。
如代码中的 new_date = now + delta，将当前日期时间 now 增加了 5 天得到新的日期时间 new_date。

3. datetime 对象的创建
使用构造函数：可以直接使用 datetime.datetime(year, month, day, [hour, minute, second, microsecond]) 
构造函数创建 datetime 对象。例如代码中的 date1 = datetime.datetime(2025, 2, 20) 和 date2 = datetime.datetime(2025, 2, 12) 
分别创建了两个不同日期的 datetime 对象。

4. 日期时间的减法运算
计算时间差：两个 datetime 对象相减会得到一个 timedelta 对象，该对象表示两个日期时间之间的差值。
如代码中的 diff = date1 - date2，计算出 date1 和 date2 之间相差 8 天，diff 是一个 timedelta 对象，
其输出形式为 8 days, 0:00:00。

5. 获取当前日期时间
使用 now 方法:datetime.datetime.now() 方法可以获取当前的日期和时间，返回一个 datetime 对象。
例如代码中的 now = datetime.datetime.now() 就获取了程序运行时的当前日期时间。

"""
import datetime

date_str = "12-02-2025 14:30"
date_obj =datetime.datetime.strptime(date_str,"%d-%m-%Y %H:%M")
print(date_obj)

now = datetime.datetime.now()
delta = datetime.timedelta(days=5)#增加了5天
new_date = now + delta
print(new_date)

date1 = datetime.datetime(2025,2,20)
date2 = datetime.datetime(2025,2,12)
diff = date1 - date2
print(diff)#8

