# break example
# n=0
# while n<5:
#     n +=1
#     if n == 3:
#         break
#     print (n)
# print ("最后的一项",n)

# continue example
# n=0
# for x in range(6):
#     if x % 2 == 0: #x是偶数
#         continue # 符合条件,会忽略下面的程式
#     print (x)
#     n +=1
# print ("最后一项",n)

# else example
# sum = 0
# for n in range (11):
#     sum += n
# else:
#     print (sum) #印出最后的总和

# 综合范例：找出整数平方根
# x = int(input("输入一个正整数："))
# for i in range (x+1): # 从0开始，直到 x-1 
#     if i*i == x:
#         print ("整数平方根",i)
#         break # 符合条件就会强制结束回圈，不会执行 else 区块
# else:
#     print ("没有整数平方根")
