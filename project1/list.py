bicycles = ['trek', 'cannondale', 'redline', 'specialized']
bicycles.append('lineway')
bicycles.insert(2,'bus')
print(bicycles[-1].title())
print(bicycles)
del bicycles[0]
print(bicycles)


names=['zzx','yyq','xlp']
print('\tDear '+names[0]+names[1]+names[2]+'\n请您前来参加聚餐～')
print(names[2]+"有事不能前来")
names[2]="ljc"
print('\tDear '+names[0]+names[1]+names[2]+'\n请您前来参加聚餐～')
print("找到了更大的餐桌")
names.insert(0,'lcc')
names.insert(3,"hk")
names.append("lcg")
print('\tDear '+names[0]+names[1]+names[2]+names[3]+names[4]+names[5]+'\n请您前来参加聚餐～')
print('新购买的餐桌无法及时送达，因此只能邀请两位嘉宾')
print(names.pop()+"sorry很抱歉，无法邀请你来共进晚餐。")
print(names.pop()+"sorry很抱歉，无法邀请你来共进晚餐。")
print(names.pop()+"sorry很抱歉，无法邀请你来共进晚餐。")
print(names.pop()+"sorry很抱歉，无法邀请你来共进晚餐。")
print(names[0]+names[1]+"你们仍在名单内")
del names[1],names[0]
print(names)


places=["beijing","shijiazhuang","dezhou","dalian","shanghai"]
print(places)
print(sorted(places))
print(places)
print(sorted(places,reverse=True))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)
print(places.__len__())

# 循环列表
pizzas=["zhizun","haixian","liulian"]
for pizza in pizzas:
    print("I like "+pizza+" pizza!")
print("I really love pizza!")

# 数字列表
values=[]
for value in range(1,21,2):
    values.append(value)
print(values)
numbers=[]
for value in range(1,1000001):
    numbers.append(value)
    #print(value)
print(min(numbers))
print(max(numbers))
print(sum(numbers))

numbers2=[]
for value in range(1,11):
    numbers2.append(value**3)
for value in numbers2:
    print(value)
#立方解析
numbers3=[value**3 for value in range(1,11)]
print(numbers3)

#切片
print("The first three items in the list are:")
print(bicycles[:3])
print("Three items from the middle of the list are:")
print(bicycles[1:4])
print("The last three items in the list are:")
print(bicycles[-3:])

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods=my_foods[:]
my_foods.append("milk")
friend_foods.append("cake")
for food in my_foods:
    print(food)
print("This is my food")
for food in friend_foods:
    print(food)
print("This is my friend food")

#元组
food_list=("apple","shala","milk","rice")
for food in food_list:
    print(food)
food_list=("apple","shala")
print(food_list)

#条件测试
alien_color="yellow"
if alien_color == "green":
    print("you got 5 score")
elif alien_color == "yellow":
    print("you got 10 score")
else:
    print("you got 15 score")

#users=[]
users=["admin","wkx","zzx","yyq","xlp"]
new_users=["wKx","Zzx","ghf","ldy","wmm"]

for user in new_users:
    if user.lower() in users:
        print("该名字已被使用")
    else:
        print("这个用户名未被使用")

if users:
    for user in users:
        if user == "admin":
            print("Hello admin, would you like to see a status report?")
        else:
            print("Hello Eric, thank you for logging in again")
else:
    print("the list is null")

numbers4=[]
for number in range(1,10):
    numbers4.append(number)
for number in numbers4:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd ")
    else :
        print(number.__str__()+"th")

