# 3-1 print with index
names=["jinkun","oonteng","weiann","leeyang","jiazhen"]
print (names[0])
print (names[1])
print (names[2])
print (names[3])
print (names[4])

# 3-2 combine name with greeting
for x in names:
    print ((x)+" Hi!")

'''
add item
1. append : add item to last position of list
2. insert : add item to given index 
    e.g. (2,'new item')

delete itemgit a
1. del : delete item by index(postion)
    e.g. del list[0]
2. pop(): delete last item in list
    / or pop (index): delete specified item
3. remove : delete specified item
    e.g remove ("specified item")

'''
# 3-4 create guest list (3 ppl)
guest_list = ["Chai", "Jin", "Kun"]
invite_msg = " , you are invited to the party!"
print (guest_list[0] + invite_msg)
print (guest_list[1] + invite_msg)
print (guest_list[2] + invite_msg)

# 3-5 replace one person for absent
print (guest_list[1] + " replied that he can't make it")
guest_list[0] = "US Boy"

# 3-6 invite more people
print ("changed table which allow more people to join!")
guest_list.insert(0,"JK")
guest_list.insert(2,"yang berhormat")
guest_list.append("ft. Malaysian")

for x in guest_list:
    print (x + invite_msg)
print (guest_list)

# 3-7 table dagamed, back to 2 person
print ("Sry guys, I apologized as only two person could fit")
guest_list.pop(0)
guest_list.pop(0)
guest_list.pop(0)
guest_list.pop(2)

print (guest_list[0] + " , you are still welcome to the party!")
print (guest_list[1] + " , you are still welcome to the party!")

del guest_list[0]
guest_list.remove("Kun")
print(guest_list)

# 3-8 trip checklist
places = ["Japan", "Taiwan", "China", "Thailand", "HongKong"]
print(places)

places_sorted = sorted(places)
print(places_sorted)

places.reverse()
print(places)

places.sort()
print(places)

places.sort(reverse=True)
print(places)
