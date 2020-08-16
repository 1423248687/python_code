# 把每个单词的首字母变成大写
name = "wo shi zhu"
print(name.title())
# 把每个字符变成大写
print(name.upper())
# 把每个字符都变成小写
print(name.lower())
# 字符串拼接
frist_name = "wo"
mid_name = "shi"
end_name = "zhu"
print(frist_name+"  "+mid_name+end_name)
# 制表符和换行符的使用
print("wo shi\tzhu\nni ne")
# 删除多余的空格
name1 = "  pig  "
print(name1)
# 删除头部的空格
print(name1.lstrip())
# 删除尾部的空格
print(name1.rstrip())
# 删除首尾的空格
print(name1.strip())
# str() 把非字符串值转化为字符串
age = 18
print("i'am"+" "+str(age)+" "+"years!")
# 四则运算
print(((1+1)*(3-1) ** 3-16/2))
import this