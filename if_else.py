# 简单的if语句
# 等于
name = ['zhangsan','lisi','wangwu','zhaoliu']
for n1 in name :
    if n1 == 'lisi':
        print(n1.upper())
    else:
        print(n1.title())
# 不等于
for n1 in name:
    if n1 != 'lisi':
        print(n1.title())
    else:
        print(n1.upper())
# and or
num = list(range(1,10))
print(num)
for n in num:
    if n/2 == 4 and n/4 ==2:
        print(n)
    else:
        if n/3 == 2 or n/5 == 1:
            print(n)
        else:
            print('nono')

# 检查特定值是否在列表中
if 3 in num:
    print("this num in list")
# 检查特定值是否不再列表中
if 30 not in num:
    print("this num not in list")
# 多次判断
num = list(range(1,10,2))
for n in num:
    if n<3:
        print('this'+" is low")
    elif 3<n<=6:
        print('this'+" is mid")
    elif n>6:
        print('this'+ " is up")
# 判定列表不为空
book = []
if book:
    print("having book")
else:
    print("no having book")

