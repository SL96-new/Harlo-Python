# 10-1 try open file
file_path = "C:\Users\Admin\Documents\Harlo-Python\learning_python.txt"
with open(file_path) as file_object:
    content = file_object.read()
    print(content)

    for line in file_object:
        print(line)

    lines = file_object.readlines()
    for line in lines:
        print (line.rstrip())


# 10-3 file open ('write mode')
filename = 'guest.txt'
with open(filename,'w') as file_object:
    file_object.write(input("please enter username: "))
