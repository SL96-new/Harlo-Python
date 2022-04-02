# 6-1 Person Information
from multiprocessing.managers import Namespace


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
