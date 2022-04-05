# 8-2 define a simple function
def favorite_book(title):
    '''显示喜欢的书本'''
    print("One of my favorite book is "+ title)

favorite_book("Harry Potter")

# 8-3,4 运用实参 arguments 的三种形式
def make_shirt (size, printing = "I love Python"):
    print ("Your shirt is " + size + " with the printing '" + printing +"'")

make_shirt("L")
make_shirt("M")
make_shirt("M","YOLO")

# 8-7 function with dictionary
def make_album(singer,album,songs=''):
    album = {'Singer':singer,'Album':album}
    if songs:
        album["Songs"] = songs
    return album

album_info = make_album('BlackPink',"THE ALBUM",8)
print (album_info)
album_info = make_album('Ed Sheeran','X')
print (album_info)

# 8-8 Function, Dictionary & While loop
def make_album(singer_name,album_name,songs_num):
    album = {"Singer":singer_name,"Album":album_name}
    if songs_num:
        album["Song"]=songs_num
    return album

while True:
    singer_name = input("Please enter singer's name\n(enter 'q' at any time to quit) :")
    if singer_name == 'q':
        break
    album_name = input("Please enter album's name\n(enter 'q' at any time to quit) :")
    if album_name == 'q':
        break
    songs_num = input("Please enter number of songs\n(enter 'q' at any time to quit) :")
    if songs_num == 'q':
        break

album_info = make_album(singer_name,album_name,songs_num)
print (singer_name + "'s " + album_name + " have " + songs_num + " songs!")

# 8-9, 10, 11 create function combine with list
def show_magician(magicians,great_magicians):
    while magicians:
        magicians_list = magicians.pop()
        great_magicians.append(magicians_list)

def make_great(great_magicians):
    for magician in great_magicians:
        great_title = "The Great " + magician
        print(great_title)
    
magicians = ["Henry","Eddie","Jimmy","Lois","Emma"]
great_magicians=[]

show_magician(magicians[:],great_magicians)
make_great(great_magicians)

print (magicians)

# 8-11 任意数实参练习
def make_sandwiches (*ingredients):
    print("\nMaking a sandwich with the following ingredients:")
    for ingredient in ingredients:
        print (ingredient)

make_sandwiches("egg")
make_sandwiches("cheese","chicken strip","lettuce","egg")
make_sandwiches("chili sause","tuna","corns","cucumber","beef pepperoni")

# 8-13 任意数量的关键字实参练习
def build_profile(first, last, **info):
    profile ={}
    profile["first_name"] = first
    profile["last_name"] = last
    for keys, values in info.items():
        profile[keys] = values
    return profile

SL = build_profile ("Shao Lun", "Ng", age ="26", country = "Malaysia")
print(SL) 