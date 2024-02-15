a=int(input('Enter first number: '))
b=int(input('Enter second number: '))
c=int(input('Enter third number: '))

if a>b and a>c:
    print('a is biggest number')
elif b>c:
    print('b is biggest number')
elif a==b and a==c:
    print('a and b and c are equal')
elif a==b:
    print('a and b are equal')
elif a==c:
    print('a and c are equal')
elif b==c:
    print('b and c are equal')
else:
    print('c is biggest number')