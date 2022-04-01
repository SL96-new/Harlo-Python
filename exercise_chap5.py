# 5-3,4,5 alien color games
alien_color = "green"
if alien_color == "green":
    scores = 5
elif alien_color == "yellow": 
    scores = 10
else:
    scores = 15
print ("you get "+ str(scores) + " marks!")

# 5-6 different stages based on ages
age = 26
if age <2:
    stage = "baby"
elif 2 <= age < 4:
    stage ="toddler"
elif 4 <= age < 13:
    stage ="child"
elif 13 <= age < 20:
    stage ="teenager"
elif 20 <= age < 65:
    stage ="adult"
elif age >= 65:
    stage ="elderly"

print("you are in the stage of "+ stage +"!")

# 5-7 check whether in list
favourite_fruit = ["apple","orange","kiwi","grapes"]
if "apple" in favourite_fruit:
    print ("you really like apple!")
if "durian" in favourite_fruit:
    print ("you really like durian!")
if "kiwi" in favourite_fruit:
    print ("you really like kiwi!") 

# 5-8 greeting to users
users = ["Kingsley","John","Tom","Admin","Hailey","Emma"]
for user in users:
    if user == "Admin":
        print ("Hello" + user + ", would you like to see a status report?")
    else:
        print ("Hello " + user + ", thank you for logging in again")

# 5-9 empty list check
users = []
if users == []:
    print ("We need to find some users!")

# 5-10 check user_name existed？
current_users = ["Kingsley","John","Tom","Admin","Hailey","Emma"]
current_users = [current_user.lower() for current_user in current_users]
new_users = ["JK","ToM","Ashley","Vincent","EMMA"]

for new_user in new_users:
    if new_user.lower() in current_users:
        print ("Sorry, this username existed, please fill in again")
    else:
        print ("this username have not been use")

# 5-11 序号排列
nums = [x for x in range (1,11)]
for num in nums:
    if num == 1:
        print (str(num) +"st")
    elif num == 2:
        print (str(num) +"nd")
    elif num == 3:
        print (str(num) + "rd")
    else:
        print (str(num) +"th")