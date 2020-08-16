# while循环
num = 1
while num <= 5:
    print(num)
    num = num+1
# 小试牛刀
num = input("请输入：")
num = int(num)
if num != 100:
    print(num)
    while num != 100:
        num = int(input("输入错误，请重新输入:"))
        if num != 100:
            print(num)
        else:
            print("牛逼")
else:
    print("牛逼！")
# 使用flag
flag = True
while flag:
    opt = input("你的操作是：")
    if opt != 'quit':
        print(opt)
    else:
        flag = False
# break的使用
while  True:
    city = input("你所在的城市：")
    if city == 'quit':
        break
    else:
        print(city)
print('thanks you!')
# continue的使用
sum = 0
while True:
    num = int(input("请输入"))
    if num % 2 == 0 :
       num+=num
    else:
        continue
    sum+=num
    if sum > 20:
        break
    else:
        print(sum)
print(sum)
# 案例 用户验证   在列表间移动元素
unconfirmed_users = ['zhangsan','lisi','wangwu','zhaoliu']
confirmed_users = []
while unconfirmed_users:
    print('unconfirmed_users : ' + str(unconfirmed_users))
    current_user = unconfirmed_users.pop()
    print('current_user '+ current_user)
    confirmed_users.append(current_user)
    print('confirmed_users :'+str(confirmed_users))
for name in confirmed_users:
    print(name)

# 案例 调查问卷 使用用户输入来填充字典
responses ={}
flag = 0
while True:
    if flag >= 3:
        break
    name = input("你的名字是：")
    response = input("你的回答是：")
    responses[name] = response
    flag += 1
for name,response in responses.items():
    print("name is "+str(name)+" ,response is "+str(response))