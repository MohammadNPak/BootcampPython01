# a = input("please enter your number (4 digit is allowed):")
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])
# print(int(a[0])+int(a[1])+int(a[2])+int(a[3]))

# if شرط :
#     دستورات
#     # indent

# a=input()
# b=3

# if int(a)>10**4:
#     print("a>b")
# else:
#     print('a<b')

# >
# <
# >=
# <=
# !=
# ==

# valid_username="mohammad"
# valid_password="123"
# username=input('please enter your username')

# password=input('please enter your password')

# if username==valid_username:
#     if valid_password==password:
#         print('welcome')
#     else:
#         print('password in wrong')
# else:
#     print('username is wrong')

# and 
# or 
# not

# x1      x2      x1 and x2       x1 or x2        not x1
# False   False   False           False           True
# False   True    False           True            True
# True    False   False           True            False
# True    True    True            True            False

# 'ali' and 10


# valid_username1="mohammad"
# valid_username2="ali"
# valid_password1="123"
# valid_password2="321"

# username=input('please enter your username')
# password=input('please enter your password')

# if username==valid_username1:
#     if password==valid_password1:
#         print(f'welcome {username}')
#     else:
#         print('password in wrong')
# else:
#     if username==valid_username2:
#         if password==valid_password2:
#             print(f'welcome {username}')
#         else:
#             print('password in wrong')
#     else:
#         print('access is denied!')

# ctlr +[  
# ctrl+ ]


# if username==valid_username1 and password==valid_password1:
#     print(f'welcome {username}')
# else:
#     if username==valid_username2 and  password==valid_password2:
#         print(f'welcome {username}')
#     else:
#         print('access is denied!')


# if شرط:
#     دستورات1
# elif شرط:
#     دستورات 
# elif شرط:
#     دستورات 
# elif شرط:
#     دستورات 
# elif شرط:
#     دستورات 
# else:
#     دستورات آخر

# if username==valid_username1 and password==valid_password1:
#     print(f'welcome {username}')
# elif username==valid_username2 and  password==valid_password2:
#     print(f'welcome {username}')
# else:
#     print('access is denied!')


# کودک <12
# نوجوان <18
# جوان <30
# بزرگسال

# age = int(input())

# if age<12:
#     print('کودک')
# elif age<18:
#     print('نوجوان')
# elif age<30:
#     print('جوان')
# else:
#     print('بزرگسال')


# while شرط:
#     دستورات

# while 1:
#     print("salam")


# a = 0
# while a<= 100:
#     print(a)
#     a= a+2

n = int(input()) #5
# 1*2*3*4*5*6*7*...*n
a=1
f = 1
while a<=n:
    f = f*a
    a=a+1
print(f)
