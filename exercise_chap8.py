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
# def make_album(singer_name,album_name,songs_num):
#     album = {"Singer":singer_name,"Album":album_name}
#     if songs_num:
#         album["Song"]=songs_num
#     return album

# while True:
#     singer_name = input("Please enter singer's name\n(enter 'q' at any time to quit) :")
#     if singer_name == 'q':
#         break
#     album_name = input("Please enter album's name\n(enter 'q' at any time to quit) :")
#     if album_name == 'q':
#         break
#     songs_num = input("Please enter number of songs\n(enter 'q' at any time to quit) :")
#     if songs_num == 'q':
#         break

# album_info = make_album(singer_name,album_name,songs_num)
# print (singer_name + "'s " + album_name + " have " + songs_num + " songs!")
