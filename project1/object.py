from method import  make_shirt as shirt

shirt("red","s")
#字典
person={'first-name':'zhao','last-name':'zixu','age':23,'city':'beijing'}
print(person['first-name'],person['last-name'],person['age'],person['city'])

favorite_languages = { 'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python' }
people=['jen','zzx','wkx']
for p in people:
    if p in favorite_languages.keys():
        print("您已参与调查")
    else:
        print(p+" 邀请您参与调查")
for key in favorite_languages.keys():
    print(key)
for value in favorite_languages.values():
    print(value)

#用户输入
message=input("please input something:")
print(message)

number=input("please input a number:")
number=int(number)
if number % 10 == 0:
    print(str(number)+"是10的整数倍")
else:
    print(str(number)+"不是10的整数倍")

#while循环
number=0
active = True
while active:
    number=input("please input a number")
    if str(number)=="quit":
        break
    print(number)
#    if int(number) > 4:
 #       active = False

#列表转移
sandwich_orders=['apple','pastrami','orange','pear','pastrami']
finished_sandwiches =[]

while 'pastrami' in sandwich_orders:
    print("pastrami卖光了")
    sandwich_orders.remove('pastrami')
for sandwich in sandwich_orders:
    print("I made your "+sandwich+" sandwich")
while sandwich_orders:
    finish=sandwich_orders.pop()
    finished_sandwiches.append(finish)
print(finished_sandwiches,sandwich_orders)

#调查
places={}
flag = True
while flag:
    user = input("What's your name?")
    place = input("\nIf you could visit one place in the world, where would you go?")
    places[user]=place
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        flag = False
for name,place in places.items():
    print(name+"like"+place)

