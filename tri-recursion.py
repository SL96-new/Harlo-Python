## run tri recursion

## recursive function
## 回归函数
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)


def tri_recursion(k):
  if(k > 0):
    result = k + k - 1        
    print(result)
  else:
    result = 0
  return result


'''
k chain:
6 --> 5 --> 4 --> 3 --> 2 --> 1 --> 0
1 to 1 relationship

1 to many relationship
many to many relationship

return chain:
21 <-- 15 <-- 10 <-- 6 <-- 3 <-- 1 <-- 0

Hashing
Pointer

JavaScript: Prototype | --> 1 --> .....
                      | --> 2 --> 7 | --> 8
                                    | --> 10
                                    | --> 100
                      | --> 3 | --> 4
                              | --> 5

3 > 0 == True
input <------ 3 
result = 3 + tri(3 - 1)

tri(3 - 1):
--2 > 0 == True
--input <------ 2 
--result = 2 + tri(2 - 1)

tri(2 - 1):
----1 > 0 == True
----input <------ 1 
----result = 1 + tri(1 - 1)

tri(1 - 1):
------1 > 0 == False
------result = 0
----return 0

return 0 --> tri(1 - 1):
----input <------ 1 
----result = 1 + 0
----print(1)

--return 1
--input <------ 2 
--result = 2 + 1

'''