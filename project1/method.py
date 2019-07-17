#函数

def make_shirt(size,color='black'):
    print("This shirt is "+size+" and the color is "+color+"!")

make_shirt(size="l")
make_shirt(size="m",color="red")
make_shirt(size="s",color="white")

def city_country(city,country):
    print(city+" is in "+country)
    return city+","+country

message=city_country("Santiago","Chile")
print(message)

def show_magicians(magicaians):
    for magician in magicians:
        print(magician)

def make_great(magicaians):
    magic=[]
    for magician in magicians:
        magician="the Great "+magician
        magic.append(magician)
    return magic


magicians=["liuqian","chsiud","jxisj"]
magicians=make_great(magicians)
show_magicians(magicians)



def make_album(singer,music,number=0):

    if number:
        song = {'singer': singer, 'music': music,'number':number}
    else:
        song = {'singer': singer, 'music': music}
    return song

while True:
    print("please input your favourite singer and his song")
    print("you can input 'q' to quit")
    singer=input("please input your favourite singer")
    if singer == "q":
        break;
    song=input("please input his song")
    if song == "q":
        break;
    songs=make_album(singer,song)
    print(songs)

