from typing import Any
# names: list[str] = ['Bassam','jny','muhammad']
# for name in names :
#     print(f'A.O.A {name}')
#     print("Java developer\n")
# print("Pakistan zinda'abad")

# i: int = 0
# while i < len(names):
#     print(f'Hello turkey ' + names[i].title())
#     i+=1
    
data_base : list[tuple[str,str]] = [("qasim",'123'), #tuple is unmutable
                                    ("sirzia",'345'),#it can also be a list of list
                                    ('ikhlas','789')
                                    ]

# for row in data_base:
#     print(row)
#     user,password = row
#     print(user,password)
# input_user : str = input('Enter user Name')
# input_password : str = input('Enter user Password')
# for row in data_base :
#      user,password = row
#      if input_user == user and input_password == password:
#         print("Valid user")
# else:
#          print("invalid ")
         

magicians: list[str] = ['alice', 'david', 'carolina']
# for magician in magicians:
#     print(f"{magician.title()}, that was a great trick!")
    

# print(f"I can't wait to see your next trick, {magician.title()}.\n") #there is no scope of local or global u can use it outside the loop pr sirf last wali
#identation matters a lot in python otherwise it will generate error
# print(list(enumerate(magicians)))
# for index , names in enumerate(magicians):
#     print(index,names)
    
# print(list(range(2,11,2))) #all even number list
    
# for n in range(1,11,2): #all odd numbers
#     print(n)


# for n in range(1,11,1):
#     print(f'2 x {n} = {2*n}')
    
# squares:list[int] = []
# for value in range(1, 11):
#     square = value ** 2
#     squares.append(square)
# print(squares)

# List comprehensive
# for item in items_list:
#     loop_body
# Comprehensive Style
# [loop_body for item in items_list]

# print([i**2 for i in range(1,11)])


digit :list[int] = [1,3,6,8,3,4,8]
# print(max(digit))
# print(min(digit))
# print(sum(digit))
print(type(digit))
# print(digit.count(max(digit)))

print(sorted([3,4,1,6]))

Tup:tuple[Any] = (12,34,'abc')
print(type(Tup))