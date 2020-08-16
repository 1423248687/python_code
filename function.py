# 函数的定义
def greet():
    """这是一个简单的函数"""
    print("hello world")
greet()
def print_username(username):
    """打印用户名"""
    print("你的名字是"+str(username))
print_username('张三')

# 位置实参
def describe_name(person_name,person_languages):
    print("my name is "+person_name)
    print("I like "+person_languages)
describe_name('zhangsan','python')
describe_name(person_languages='java',person_name='lisi')

# 有返回值的函数
def your_name(first_name,last_name):
    """返回全名"""
    full_name = first_name+last_name
    return full_name
full_name = your_name('zhang','san')
print(full_name)

# 可选的实参
def person_info(person_name,person_languages,person_age = ''):
    if person_age:
        msg = 'my name is '+person_name+" ,I am "+person_age+' ,and I like '+person_languages
    else:
        msg = "my name is "+person_name+" ,I like "+person_languages
    return msg
msg = person_info('zhangsan','java',)
print(msg)
msg = person_info('lisi','python','18')
print(msg)

# 返回字典
def name_info(first_name,last_name):
    name = {'first':first_name,'last':last_name}
    return name
name = name_info('zhang','san')
print(name)

# 小测试1
def person_name(first_name,last_name,age = ''):
    name = {'first':first_name,'last':last_name}
    if age != '':
        name["age"] = age
    return name
name = person_name('li','si','18')
print(name)

# 小测试2
# def test_info(first_name,last_name,age = ''):
#     name = {'first':first_name,'last':last_name}
#     if age != '':
#         name['age'] = age
#     return name
# while True:
#     first_name = input("your firstname : ")
#     last_name = input("your lastname : ")
#     age = input("your age : ")
#     person = test_info(first_name,last_name,age)
#     print(person)

# 传递列表
def greet_users(names):
    for name in names:
        print("hello! "+ name)
names = ['zhangsan','lisi','wangwu','zhaoliu']
greet_users(names)

# 修改列表
def name_change(name_after,name_last):
    while name_after:
        print(name_after)
        name_current = name_after.pop()
        print("current name is " +name_current)
        name_last.append(name_current)
        print(name_last)
    return name_last
def show_name(names):
    for name in names:
        print("I am "+name)
name_after = ['zhangsan','lisi','wangwu','zhaoliu']
name_last = []
name = name_change(name_after,name_last)
show_name(name)
print('--------------------------')
show_name(name_after)
print('--------------------------------')
show_name(name_last)
print('-----------------------------------------------')

# 禁止修改列表
name_last = name_change(name_last,name_after)
show_name(name_last)
print('-------------------------------')
show_name(name_after)


# 传递任意数量的实参
def read_book(*books):
    for book in books:
        print("I like "+book)
read_book('english')
print('\n')
read_book('english','chinese','physical')

# 使用位置实参和任意数量的实参
def love_languages(name,*languages):
    print('my name is ' +name)
    for l in languages:
        print('this is '+str(l))
love_languages('zhangsan','C','python','java')

# 使用任意位置的关键字实参
def build_profile(first,last,**person_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key,value in person_info.items():
        profile[key] = value
    return  profile
profile = build_profile('zhang','san',location='changsha',age = '18')
print(profile)