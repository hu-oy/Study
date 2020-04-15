import re

pattern =r"\d+"
s="2019/4/23,海军70年"

it =re.finditer(pattern,s)
#print(dir(next(it))
for i in it:
    print(i.group())

obj = re.match(r"[A-Z]\w+","Hello World")
print(obj.group())