# 7-3 检查是否为 10 的倍数
number = input("Enter a number, and I'll tell you if it can divided by 10: ")
number = int(number)
if number % 10 == 0:
    print("\nThe number " + str(number) + " can divide by 10!")
else:
    print("\nThe number " + str(number) + " could not divide by 10.")

# 7-4 pizza topping (While loop)
prompt = "\nPlease enter any topping you would like to add"
prompt += "\nEnter 'quit' while finished :"

message = ''
while message != "quit":
    message = input(prompt)
   
    if message != 'quit':
        print ("\nYou have selected " + message + " on your pizza!")
    elif message == 'quit':
        print ("Order received, preparing your pizza soon.")

# 7-5 Movie Ticket (while loop + if + break)
prompt = "\nPlease enter your age, ticket price will count based on your age."
prompt += "\nEnter '0' while finished :"

age = ''
while age != 'quit':
    age = input(prompt)
    age = int(age)
    if age == 0:
        break
    elif age <= 3:
        print ("Your movie ticket is FREE!")
    elif age <=12:
        print ("Your tickey price is $10")
    elif age > 12:
        print ("Your ticket price is 15")

# 7-8 While loop (with list)
sandwich_orders = ["tuna","pastrami","mayo_egg","pastrami","chicken_strip","pastrami","beef_ball"]
finished_sandwiches = []

while sandwich_orders:
    processing_sandwich = sandwich_orders.pop()
    
    print(processing_sandwich.title() + " sandwich is making!")
    finished_sandwiches.append(processing_sandwich)

print ("\nThe following sandwich on list:")
for finish_sandwich in finished_sandwiches:
    print (finish_sandwich.title())

# 7-9 delete specific item in list (with While loop)
while 'pastrami' in finished_sandwiches:
    finished_sandwiches.remove ('pastrami') 
print (finished_sandwiches)

# 7-10 dream place list (while loop + dictionary)
response = {}
polling_status = True       # 置放标志（便于判断、控制)

user = "please enter your name: "
message = "please enter place you would like to visit: "

while polling_status:
    username = input(user)
    place = input(message)
    response[username]=place

    condition = input("Would you like to let another person respond? (yes/ no) :")
    if condition == 'no':
        break

print ("--- Result ---")
for username, place in response.items():
    print (username + " would like to visit " + place)
