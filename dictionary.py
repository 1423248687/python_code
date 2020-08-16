# 定义
person = {'name':'zhangsan','age':'18'}
print(person['name'])
print(person['age'])
print(person)
# 添加键值对
person['english'] = 100
person['love'] = 'book'
print(person)
# 修改字典的值
person['name'] = 'lisi'
print(person)
# 删除键值对
del person['love']
print(person)
# 定义多个字典
code_languages = {
    'zhangsan':'C',
    'lisi':'Java',
    'wangwu':'C#',
    'zhaoliu':'python'
}
print(code_languages)
# item()遍历
for key,value in code_languages.items():
    print("key: "+key)
    print("value: "+value+'\n')
# key()遍历字典中所有的键名
for name in code_languages.keys():
    print("\n name: "+name)
# 小测试1
names = ['lisi','zhaoliu']
for name,languages in code_languages.items():
    if  name in names:
        print(name.title()+",you like "+code_languages[name].upper())
# 小测试2
for name in names:
    if name in code_languages.keys():
        print(name.title()+",you like "+code_languages[name])
# 使用sorted()对字典的键进行临时的排序
print("\n")
for name in sorted(code_languages.keys()):
    print(name + ",you like "+code_languages[name])
# 使用values()遍历字典中的值
for languages in code_languages.values():
    print(languages.title())
# 集合(set) 每一个值都是独一无二的
code_languages['liuliu'] = 'php'
code_languages['wangba'] = 'php'
print(code_languages)
for languages in set(code_languages.values()):
    print(languages)
# 列表中存储字典
person_1 = {'name':'zhangsan','class':'01'}
person_2 = {'name':'lisi','class':'02'}
person_3 = {'name':'wangww','class':'03'}
person = [person_1,person_2,person_3]
print(person)
for p in person:
    print(p)

# 小测试3
person = []
for p in range(0,30):
    new_person = {'name':'zhangsan','class':'01'}
    person.append(new_person)
for p in person[:5]:
    print(p)
# 字典中存储列表
person = {
    'name':['zhangsan'],
    'like':['book','playgame'],
    'languages':['c','php','java','python'],
}
for name,languages in person.items():
    print('name is '+ name)
    for languages in languages:
        print(languages)
# 字典中存放字典
names = {
    'zhangsan':{
        'like':'book',
        'grade':'100',
        'languages':'c',
    },
    'lisi':{
        'like':'sport',
        'grade':'99',
        'languages':'php',
    }
}
for name,name_info in names.items():
    print('my name is '+name)
    print('i like '+name_info['like']+', and I grade is '+name_info['grade']+', and my languages is '+name_info['languages'])
