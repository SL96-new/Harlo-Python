# 6-1 Person Information
SL = {"first_name":"SL","last_name":"N","age":"26","city":"KL"}
for k,v in SL.items():
    print ("\nKey:" + k)
    print ("Value:" + v)

# 6-2 favourtie num (>Birthday)
Birthday = {"JinKun":"0806","LeeYang":"0626","OonTeng":"0928","JiaZhen":"0302","Weiann":"0731"}
for name,date in Birthday.items():
    print (name + "'s birthday is " + date)

# 6-6 check whether took poll
names = ["Alex","Ben","Tom","Henry","Jiimy"]
responses = {"Alex":"Python","Tom":"C+","Henry":"Java"}

for name in names:
    if name in responses.keys():
        print (name + ", Thanks for taking poll!")
    else:
        print (name + ", please pick your answer!")

# 6-7 Nested Dictionary in List
SL = {"first_name":"Shao Lun","last_name":"Ng","age":"26"}
JK = {"first_name":"Jin Kun","last_name":"Chai","age":"26"}
OT = {"first_name":"Oon Teng","last_name":"Wong","age":"28"}
people = [SL,JK,OT]

for person in people:
        print ("Full Name:" + person["first_name"] + " " +person["last_name"])
        print ("Age:" + person["age"])

# 6-10 Nested list in Dictionary [Favourite Num]
Fav_nums = {
    "JinKun":["0806","1996"],
    "LeeYang":["0626","8","1010"],
    "OonTeng":["0928","0214"],
    "JiaZhen":"0302",
    "Weiann":["0731","88"],
    }

for name,numbers in Fav_nums.items():
    print (name.title() + " favourite number are:")
    for number in numbers:
        print ("\t" + number)
