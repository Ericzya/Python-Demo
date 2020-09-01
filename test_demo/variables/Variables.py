# 整形
a = 100
# 浮点型
b = 100.0
# 字符串
c = "100"

print(a)
print(b)
print(c)

# 更改变量类型
c = 100
print(c)

# 集中赋值
d = e = f = 1
print(d, e, f)
# 测试引用传递还是值传递
d = 2
print(d, e, f)

# 删除e
del e

# 分别赋值
g, h, i = 1, 2, 3
print(g, h, i)

# 给字符串赋值
s = "abide"
print("打印截取字符串" + s[1:3])
