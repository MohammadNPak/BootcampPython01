
# n = 10 

# n! = 1*2*3*4*5*6*7*8*9*10
# n! = n*(n-1)!

# 10! = 10*(10-1)!=10*9!
# 9!  = 9*(9-1)!=9*8!
# 8! = 8*7!
# 7! = 7*6!                       
# 6! = 6*5!                       6! = 6*120 = 720
# 5! = 5*4!                       5! = 5*24=120
# 4! = 4*3!                       4! = 4*6 = 24
# 3! = 3*2!                       3! = 3*2 = 6
# 2!= 2*1!                        2! = 2*1 = 2
# 1! = 1*0!                       1! = 1*1 = 1
# 0! = 1                          

# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         n_1=factorial(n-1)
#         return n*n_1

# print(factorial(1000))
# from pathlib import Path

# data_address = Path('data\data.txt')
# f = open(data_address,'r')
# output = f.read()
# print(output)
# print(data_address.parent.resolve())


# for file in data_address.parent.iterdir():
#     print(open(file,'r').read())

# from pathlib import Path
# data_address = Path('data\download.jpg')

# f = open(data_address,'rb')
# print(f.writable())
# print(f.readable())
# bytes_ = f.read()
# bytearray_ = bytearray(bytes_)
# print(len(bytes_))
# print(len(bytearray_))
# print(bytes_[0])
# print(bytearray_[0])
# # bytes_[0] = 0
# bytearray_[0] = 0
# print(bytearray_)
# print(bytearray(f.read()))
# print(dir(f))

# 1           0
# c           2
# 12          2
# 16**1    16**0

# 12*16**1 + 2*16**0

# 194
# 11000010
# a = 0b1010
# a = 0xa
# a = 0o12
# print(bin(a))
# print(hex(a))
# print(oct(a))


# f = open('data\data.txt','r')
# print(f.read())
# f.close()

# with open('data\data.txt','r') as f:
#     output = []
#     is_first = True
#     a = f.read()
#     lines = a.split('\n')
#     for line in lines:
#         col = line.split(',')
#         if is_first:
#             keys = col
#             is_first=False
#         else:
#             info=dict.fromkeys(keys)
#             for i,key in enumerate(keys):
#                 info[key]=col[i]
#             output.append(info)
# print(output)

# import csv

# with open('data\data.csv') as f:
#     data = csv.reader(f)
#     head = next(data)
#     print(head)
#     print(data)
#     print(type(data))
#     for row in data:
#         print(row)

# import sys
# i = 100_000_000
# # a = list(range(i))
# b=range(i)
# # print(sys.getsizeof(a))
# print(sys.getsizeof(b))

output = [x**2 for x in range(10)]
output2 = (x**2 for x in range(10))
output3 = {key:value for key,value in zip(range(10),range(100,110))}

output = []
for x in range(10):
    output.append(x**2)
print(type(output2))
print(output3)


if a>0:
    b=1
else:
    b=2

b = 1 if a>0 else 2

b = a>0?1:2