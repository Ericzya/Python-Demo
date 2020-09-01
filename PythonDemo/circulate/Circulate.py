# while循环
a = 9999
while a > 1:
    if a % 7 == 0:
        print(a)
    a -= 1
# for循环
for letter in 'Python':
    print("当前字母为：", letter)

fruits = ['banana', 'apple', 'mango']
for fruit in fruits:
    print("当前水果为:", fruit)

# 计算质数
i = 2
while i < 999999:
    j = 2
    while j < (i / j):
        if not (i % j):
            break
        j = j + 1
    if j > i / j:
        print(i, "是质数")
    i += 1
print("计算结束")
