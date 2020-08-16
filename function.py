# 函数的定义
def greet():
    """这是一个简单的函数"""
    print("hello world")
greet()
def print_username(username):
    """打印用户名"""
    print("你的名字是"+username)
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
def person_info(person_name,person_languages,person_age =  ''):
    if person_age:
        msg = 'my name is '+person_name+" ,I am "+person_age+' ,and I like '+person_languages
    else:
        msg = "my name is "+person_name+" ,I like "+person_languages
    return msg
msg = person_info('zhangsan','java',)
print(msg)
msg = person_info('lisi','python','18')
print(msg)