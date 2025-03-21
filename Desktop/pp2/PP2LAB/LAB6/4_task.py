#Task 4 Invoke square root function after specific milliseconds(在指定毫秒后计算平方根)
import time
import math

number = 25100
delay = 2123  # 毫秒

time.sleep(delay / 1000)  # 将毫秒转换为秒

result = math.sqrt(number)
print(f"Square root of {number} after {delay} milliseconds is {result}")