# 4-1 create favourite pizza list
pizzas = ["Hawaii Chicken","Pepperoni","Spicy Seafood"]
for pizza in pizzas:
    print (("I like ")+(pizza) +(" pizza!"))
print ("I really love pizza")

# 4-3 print 1-20
for num in range(1,21):
    print (num)

# 4-4&5 sum from 1 to 1 million
number = [x for x in range(1,1000001)]
print (min(number))
print (max(number))
print (sum(number))

# 4-6 odd numbers from 1-20
odd_nums = [y for y in range(1,21,2)]
print (odd_nums)

# 4-7 3的倍数 from 3-30
nums_could_divide_by_3 = [z for z in range (3,31) if z%3==0]
print (nums_could_divide_by_3)

# 4-8&9 cube 立方
cube = [a**3 for a in range (1,11)]
print (cube)

# 4-13 buffet list (use tuple)
buffet_list=("egg","fish","chicken","pork","sushi")
for food in buffet_list:
    print(food)

buffet_newlist = list(buffet_list)
buffet_newlist [2] = "ice-cream"
buffet_newlist [3] = "ramen"

buffet_list2 = tuple(buffet_newlist)
print (buffet_list2)