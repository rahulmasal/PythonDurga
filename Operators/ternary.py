# ~a -unary operator
# a+b binary operator

# a=10
# b=20
# c=30 if a>b else 40

# print(c)

# d=int(input("enter first number: "))
# e=int(input("enter second number: "))
# min=d if d<e else e
# print("the minimum value: ",min)

a=int(input('enter first number : '))
b=int(input('enter second number : '))
# c=int(input('enter third number : '))

# min =a if a<b and a<c else b if b<c else c
# max=a if a>b and a>c else b if b>c else c
# print('min value is ',min ,'and max value is ', max)

result="Equal" if a==b else "smaller" if a<b else "Bigger"
print(result)