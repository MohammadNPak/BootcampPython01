n = int(input())

# def is_prime(n):
#     if n%2==0:
#         return False
#     for i in range(3,int(n**0.5)+1,2):
#         if n%i==0:
#             return False
#     return True

output = ""
while n>1:
    i=2
    counter = 0
    while n%i ==0:
        n = n//i
        counter+=1
    if counter>1:
        output += f"{i}^{counter}*"
    elif counter==1:
        output += f"{i}*"

    i=3
    while i<n:

    # for i in range(3,n+1,2):
        counter = 0
        while n%i ==0:
            n = n//i
            counter+=1
        if counter>1:
            output += f"{i}^{counter}*"
        elif counter==1:
            output += f"{i}*"
        i=i+2

print(output[:-1])





# def is_prime(number):
#     if number == 2:
#         return True
#     elif number % 2 == 0:
#         return False
#     else:
#         for i in range(3, int(number**0.5)+2, 2):
#             if number % i == 0:
#                 return False
#         return True


# def prime_factors(number: int):
#     output: str = ""
#     factor = 2
#     while number > 1:
#         power = 0
#         while number % factor == 0 and is_prime(factor):
#             power += 1
#             number //= factor
#         if power > 1:
#             output = output + \
#                 f"*{factor}^{power}" if output else f"{factor}^{power}"
#         elif power == 1:
#             output = output + \
#                 f"*{factor}" if output else f"{factor}"
#         factor = 3 if factor == 2 else factor+2
#     return output


# print(prime_factors(int(input())))
