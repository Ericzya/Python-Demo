"""
多行注释（双引号）
"""
from pip._vendor.distlib.compat import raw_input

flag = False
if flag:
    print("Hello,python!")
    print("Hello,second line!")
else:
    print("Hello,python false answer")
# 这是一行测试
workDays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
dayToFly = raw_input("你想哪天上天？")
print(workDays[int(dayToFly) - 1])
