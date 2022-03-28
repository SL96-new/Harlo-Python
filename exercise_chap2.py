# 2-3 username + greeting
username = input ()
hello = "Hello " + username + ", would you like to learn some Python today?"
print (hello)

# 2-4 string.method 
print (username.lower())
print (username.upper())
print (username.title())

# 2-5 & 6 combine variable and string 
famous_person = "JK"
message = famous_person + "said: \"JUST DO IT\" "

# 2-7 try strip method
name = "\t  Emma Watson\nTom Holland\t.     "
name = name.lstrip()
name = name.rstrip()
print (name)