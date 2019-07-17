import json
import unittest
#文件操作
file="learning_python.txt"
flag=1
str=''
with open(file) as file_obiect:
    text=file_obiect.readlines()
for line in text:
    print(line.strip())
    str+=line.strip()
print(text,str.replace('1','5'))

#测试类
class Employee():
    def __init__(self,first,last,money):
        self.first=first
        self.last=last
        self.money=money

    def give_raise(self,add=5000):
        self.money+=add
        return self.money

class TestEmployee(unittest.TestCase):

    def test_give_default_raise(self):
        employee=Employee('wang','kaixin',5000);

        final=10000
        self.assertEqual(employee.give_raise(), final)

unittest.main()

#json.dump()与json.load()

filename="favourite_number.txt"
with open(filename,'w') as name_file:
    your_favourite = input("Please input your favourite number")
    json.dump(your_favourite, name_file)
with open(filename) as name_file:
    txt = json.load(name_file)
print(txt)


#将用户输入的名字存储到文件guest.txt中

with open('guest.txt','w') as name_file:
    while True:
        name = input("\nPlease input your name:")
        print("\nyou can input 'q' to quit anytime")
        if name == 'q':
            break
        else:
            name_file.write(name+'\n')

with open('guest.txt') as name_file:
    result=name_file.read()
    print(result)

#将用户输入相加
try:
    number1 = input("\nPlease input a number:")
    number2 = input("\nPlease input another number:")
    result=int(number1)+number2
except TypeError :
    print("your input is not number")

else:
    print(result)